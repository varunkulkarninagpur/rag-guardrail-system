from fastapi import FastAPI
from pydantic import BaseModel

from provider import generate_answer

app = FastAPI()

class GenerateRequest(BaseModel):
    query: str
    context: list


@app.post("/generate")
def generate(req: GenerateRequest):
    answer = generate_answer(req.query, req.context)

    return {
        "answer": answer
    }