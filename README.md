# Text Logger API

## Summary
This is my first REST API built from scratch using FastAPI. 
It allows users to create, retrieve, and delete text entries 
through clean REST endpoints. Built as part of my backend 
development learning journey.

## Key Features
- Submit text entries with author name
- Automatic word count calculation
- Retrieve all entries or one specific entry by ID
- Delete entries with proper error handling
- Auto-generated API documentation via Swagger UI

## Tech Stack

Step 1 - Create the file:

Right click in same folder → New File → name it exactly:

README.md

Step 2 — Add this content:

markdown
# Text Logger API

A REST API built with FastAPI to store and retrieve text entries.

## Tech Stack
- Python
- FastAPI
- Pydantic
- Uvicorn

## How to Run Locally

1. Install dependencies:

pip install -r requirements.txt


2. Start the server:

uvicorn text_logger:app --reload


3. Open docs:

http://127.0.0.1:8000/docs


## API Routes

| Method | Route | Description |
|--------|-------|-------------|
| GET | / | Health check |
| POST | /texts | Create a new text entry |
| GET | /texts | Get all text entries |
| GET | /texts/{id} | Get one text entry by ID |
| DELETE | /texts/{id} | Delete a text entry by ID |

Your folder should now look like this:

phase_3_fastapi/
├── text_logger.py
├── requirements.txt
└── README.md

but it has a flaw that my data is lost as soon we restart the server because the data was stored in the ram, if user submits text and server crashes the data is gone forever

## phase 4

## Database
- PostgreSQL for persistent storage
- SQLAlchemy ORM for database operations
- Auto-creates tables on startup

## Project Structure
text-logger-api/
├── text_logger.py  → API routes
├── database.py     → DB connection
├── models.py       → Table definitions
├── schemas.py      → Pydantic models
├── crud.py         → DB operations
├── requirements.txt
└── README.md