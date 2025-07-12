from fastapi import FastAPI, Request
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data
data = np.load("faq_data.npz", allow_pickle=True)
questions = data["questions"]
answers = data["answers"]
embeddings = data["embeddings"]

# Load embedding model
model = SentenceTransformer("paraphrase-MiniLM-L3-v2")

# FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Request schema
class QuestionRequest(BaseModel):
    question: str

@app.post("/get-answer")
def get_faq_answer(request: QuestionRequest):
    query = request.question.strip().lower()
    query_embedding = model.encode([query])
    _, indices = index.search(np.array(query_embedding), 1)
    matched_answer = answers[indices[0][0]]

    return {
        "answer": matched_answer
    }
