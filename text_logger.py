from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Text Logger API",
    description="A REST API to store and retrieve text entries",
    version="1.0.0"
)

# temporary in-memory storage — will replace with real DB in Phase 4
texts_db = {}
counter = 1

@app.get("/")
async def root():
    return {"message": "Text Logger API is running"}

class TextInput(BaseModel):
    content: str
    author: Optional[str] = "anonymous"

class TextResponse(BaseModel):
    id: int
    content: str
    author: str
    word_count: int

@app.post("/texts", response_model=TextResponse, status_code=status.HTTP_201_CREATED)
async def create_text(input: TextInput):
    global counter
    word_count = len(input.content.split())
    entry = {
        "id": counter,
        "content": input.content,
        "author": input.author,
        "word_count": word_count
    }
    texts_db[counter] = entry
    counter += 1
    return entry

@app.get("/texts")
async def get_all_texts():
    return list(texts_db.values())

@app.get("/texts/{text_id}", response_model=TextResponse)
async def get_text(text_id: int):
    if text_id not in texts_db:
        raise HTTPException(
            status_code=404,
            detail=f"Text with id {text_id} not found"
        )
    return texts_db[text_id]

@app.delete("/texts/{text_id}")
async def delete_text(text_id: int):
    if text_id not in texts_db:
        raise HTTPException(
            status_code=404,
            detail=f"Text with id {text_id} not found"
        )
    del texts_db[text_id]
    return {"message": f"Text with id {text_id} deleted successfully"}