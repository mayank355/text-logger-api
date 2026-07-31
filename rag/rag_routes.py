from fastapi import APIRouter
from pydantic import BaseModel
from rag import rag_engine

router = APIRouter()

class DocumentInput(BaseModel):
    doc_id: str
    text: str

class QuestionInput(BaseModel):
    question: str

@router.post("/documents")
async def add_document(input: DocumentInput):
    result = rag_engine.add_document(
        doc_id=input.doc_id,
        text=input.text
    )
    return result

@router.post("/ask")
async def ask_question(input: QuestionInput):
    result = rag_engine.rag_query(input.question)
    return result