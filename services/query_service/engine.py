import requests

RETRIEVAL_URL = "http://localhost:8001/search"
GENERATION_URL = "http://localhost:8002/generate"
VERIFY_URL = "http://localhost:8003/verify"


def process_query(query: str):
    # Step 1: Retrieval
    retrieval_res = requests.post(RETRIEVAL_URL, json={"query": query})
    context = retrieval_res.json()["results"]

    # Step 2: Generation
    gen_res = requests.post(GENERATION_URL, json={
        "query": query,
        "context": context
    })
    answer = gen_res.json()["answer"]

    # Step 3: Verification
    verify_res = requests.post(VERIFY_URL, json={
        "answer": answer,
        "context": context
    })

    verification = verify_res.json()

    return {
        "query": query,
        "context": context,
        "answer": answer,
        "verification": verification
    }