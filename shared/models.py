from pydantic import BaseModel
from typing import List, Optional

class DocumentChunk(BaseModel):
    id: str
    content: str
    metadata: Optional[dict] = {}
    score: Optional[float] = None  # Similarity score from FAISS

class QueryRequest(BaseModel):
    query: str
    top_k: int = 3

class QueryResponse(BaseModel):
    query: str
    retrieved_chunks: List[DocumentChunk]
    generated_answer: Optional[str] = None
    verification_score: Optional[float] = 0.0
    is_hallucinated: bool = False