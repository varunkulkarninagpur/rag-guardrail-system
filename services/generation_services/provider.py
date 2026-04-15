from transformers import pipeline

# Lightweight local LLM
generator = pipeline(
    "text-generation",
    model="distilgpt2",   # lightweight for now
    max_new_tokens=100
)

def generate_answer(query: str, context: list):
    context_text = "\n".join(context)

    prompt = f"""
Answer the question based ONLY on the context below.

Context:
{context_text}

Question:
{query}

Answer:
"""

    result = generator(prompt)
    return result[0]["generated_text"]