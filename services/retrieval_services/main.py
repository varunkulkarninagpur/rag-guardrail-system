from fastapi import FastAPI
from pydantic import BaseModel
import os

from utils import get_embedding, chunk_text
from database import add_embeddings, search

app = FastAPI()

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.abspath(os.path.join(BASE_DIR, "../../data/raw_docs"))
class QueryRequest(BaseModel):
    query: str


@app.post("/index")
def index_documents():
    try:
        print("DATA PATH:", DATA_PATH)

        all_chunks = []
        all_embeddings = []

        if not os.path.exists(DATA_PATH):
            return {"error": f"Path does not exist: {DATA_PATH}"}

        files = os.listdir(DATA_PATH)
        print("FILES FOUND:", files)

        if not files:
            return {"error": "No files found in raw_docs folder"}

        for file in files:
            file_path = os.path.join(DATA_PATH, file)
            print("Reading:", file_path)

            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()

                chunks = chunk_text(text)

                for chunk in chunks:
                    emb = get_embedding(chunk)
                    all_chunks.append(chunk)
                    all_embeddings.append(emb)

        add_embeddings(all_embeddings, all_chunks)

        return {
            "message": "Documents indexed successfully",
            "chunks": len(all_chunks)
        }

    except Exception as e:
        print("ERROR:", str(e))
        return {"error": str(e)}

@app.post("/search")
def search_docs(request: QueryRequest):
    query_embedding = get_embedding(request.query)
    results = search(query_embedding)

    return {"results": results}