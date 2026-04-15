from fastapi import FastAPI
from pydantic import BaseModel

from engine import verify_answer

app = FastAPI()


class VerifyRequest(BaseModel):
    answer: str
    context: list


@app.post("/verify")
def verify(req: VerifyRequest):
    result = verify_answer(req.answer, req.context)

    return result