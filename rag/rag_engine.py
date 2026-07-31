import os
import chromadb
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Groq client for LLM generation
groq_client = Groq(api_key=GROQ_API_KEY)

# ChromaDB with built-in embeddings — runs locally, no API needed
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(
    name="documents",
    metadata={"hnsw:space": "cosine"}
)

def add_document(doc_id: str, text: str):
    collection.add(
        documents=[text],
        ids=[doc_id]
    )
    return {"message": f"Document {doc_id} added successfully"}

def search_documents(query: str, n_results: int = 3):
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    return results["documents"][0]

def generate_answer(question: str, context: list):
    context_text = "\n".join(context)
    prompt = f"""Based on the following context, answer the question precisely.

Context:
{context_text}

Question: {question}

Answer:"""

    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7
    )
    return response.choices[0].message.content

def rag_query(question: str):
    relevant_docs = search_documents(question)
    answer = generate_answer(question, relevant_docs)
    return {
        "question": question,
        "answer": answer,
        "sources": relevant_docs
    }