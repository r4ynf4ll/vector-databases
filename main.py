from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from chromadb.utils import embedding_functions

app = FastAPI()

@app.get("/embed")
def embed(documents: str):
    embedder = embedding_functions.DefaultEmbeddingFunction()
    vector = embedder(documents)[0].tolist()
    return {"vector": vector}


app.mount("/", StaticFiles(directory="static", html=True), name="static")