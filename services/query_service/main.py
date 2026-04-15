from fastapi import FastAPI
from pydantic import BaseModel

from engine import process_query

app = FastAPI()


class QueryRequest(BaseModel):
    query: str


@app.post("/ask")
def ask(req: QueryRequest):
    result = process_query(req.query)

    # Decision handling
    if result["verification"]["decision"] == "REJECTED":
        result["answer"] = "⚠️ I am not confident in this answer."

    return result