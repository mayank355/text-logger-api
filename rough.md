## File 1 — database.py

This file creates the connection between FastAPI and PostgreSQL.

## 2
python
from database import Base

Importing Base from your database.py — every model must inherit from this.

python
class Text(Base):

This Python class will become a real table in PostgreSQL called texts.

python
__tablename__ = "texts"

Tells SQLAlchemy the actual table name in PostgreSQL.

python
id = Column(Integer, primary_key=True, index=True)

Auto incrementing unique ID for every row. Primary key means no two rows can have the same ID.

python
content = Column(String, nullable=False)

The text content. nullable=False means this field is required — same as Pydantic's required field.

python
author = Column(String, default="anonymous")

Optional field with default value.

python
word_count = Column(Integer)

Stores the word count automatically calculated by your API.

## 3

Pydantic and SQLAlchemy do two completely different jobs:

SQLAlchemy model  → talks to the DATABASE
                    defines table structure
                    reads/writes from PostgreSQL

Pydantic model    → talks to the USER
                    validates incoming data
                    controls what goes out in response

The flow in plain English:

User sends JSON
      ↓
Pydantic (TextCreate) validates it
— is content present?
— is it a string?
      ↓
Your function runs
      ↓
SQLAlchemy saves it to PostgreSQL
      ↓
SQLAlchemy returns a Text object
      ↓
Pydantic (TextResponse) converts it
to clean JSON for the user

Why you need both:

SQLAlchemy objects are not JSON. They're Python objects connected to a database. You can't send them directly to the user.

Pydantic converts them into clean JSON automatically.

python
# SQLAlchemy returns this — not sendable directly:
<Text object at 0x000001A2B3C4>

# Pydantic converts it to this — clean JSON:
{
    "id": 1,
    "content": "hello",
    "author": "Krish",
    "word_count": 1
}

That's exactly what from_attributes = True does — tells Pydantic how to read a SQLAlchemy object and convert it to JSON.

One line summary:

Pydantic = gatekeeper at the door (validates input, controls output)
SQLAlchemy = worker in the back (talks to database)

They never replace each other. They work together.

## pydantic
Pydantic is a Python library — not a framework.

Library   → you use it for one specific job
             Pydantic's job = data validation

Framework → controls the entire structure of your app
             FastAPI is a framework

Pydantic's one job is:

Take data → check if it matches your rules → pass or reject

That's it. FastAPI uses Pydantic internally which is why they work so well together.

## 4

do all the crud operations
 
then 
What changed from Phase 3:

python
models.Base.metadata.create_all(bind=engine)

This one line automatically creates the texts table in PostgreSQL when the server starts. You never write SQL manually.

python
db: Session = Depends(get_db)

This is dependency injection — FastAPI automatically opens a DB session for each request and passes it to your function. You just use db directly.

python
crud.create_text(db=db, text=text)

Instead of texts_db[counter] = entry you now call your crud function which saves to real PostgreSQL.