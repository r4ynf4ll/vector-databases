# filepath: /workspaces/vector-databases/main.py
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from pydantic import BaseModel
from chromadb.utils import embedding_functions
import numpy as np

app = FastAPI()
embedder = embedding_functions.DefaultEmbeddingFunction()

@app.get("/embed")
def embed_1(documents: str):
    vector = embedder([documents])[0].tolist()
    return {"vector": vector}

@app.post("/cosine_similarity")
def cos_sim(v1:str, v2:str):
    v1 = embedder([v1])[0]
    v2 = embedder([v2])[0]
    cosine_similarity = float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
    return {"cosine_similarity": cosine_similarity}

app.mount("/", StaticFiles(directory="static", html=True), name="static")
