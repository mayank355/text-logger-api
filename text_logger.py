from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Text Logger API",
    description="A REST API to store and retrieve text entries",
    version="2.0.0"
)

@app.get("/")
async def root():
    return {"message": "Text Logger API is running"}

@app.post("/texts", response_model=schemas.TextResponse, status_code=status.HTTP_201_CREATED)
async def create_text(text: schemas.TextCreate, db: Session = Depends(get_db)):
    return crud.create_text(db=db, text=text)

@app.get("/texts")
async def get_all_texts(db: Session = Depends(get_db)):
    return crud.get_all_texts(db=db)

@app.get("/texts/{text_id}", response_model=schemas.TextResponse)
async def get_text(text_id: int, db: Session = Depends(get_db)):
    text = crud.get_text(db=db, text_id=text_id)
    if text is None:
        raise HTTPException(status_code=404, detail=f"Text with id {text_id} not found")
    return text

@app.delete("/texts/{text_id}")
async def delete_text(text_id: int, db: Session = Depends(get_db)):
    text = crud.delete_text(db=db, text_id=text_id)
    if text is None:
        raise HTTPException(status_code=404, detail=f"Text with id {text_id} not found")
    return {"message": f"Text with id {text_id} deleted successfully"}