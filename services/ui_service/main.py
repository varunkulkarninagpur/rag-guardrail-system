from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import requests

app = FastAPI()

QUERY_API = "http://localhost:8004/ask"


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>RAG Guardrail System</title>
        <style>
            body { font-family: Arial; padding: 40px; background: #0f172a; color: white; }
            input { width: 60%; padding: 10px; }
            button { padding: 10px 20px; }
            .card { margin-top: 20px; padding: 20px; background: #1e293b; border-radius: 10px; }
            .accepted { color: lightgreen; }
            .rejected { color: red; }
        </style>
    </head>
    <body>
        <h1>🔥 RAG Guardrail AI</h1>

        <form method="post" action="/ask">
            <input name="query" placeholder="Ask something..." />
            <button type="submit">Ask</button>
        </form>
    </body>
    </html>
    """


@app.post("/ask", response_class=HTMLResponse)
async def ask(request: Request):
    form = await request.form()
    query = form.get("query")

    res = requests.post(QUERY_API, json={"query": query})
    data = res.json()

    decision = data["verification"]["decision"]
    score = data["verification"]["final_score"]

    color_class = "accepted" if decision == "ACCEPTED" else "rejected"

    return f"""
    <html>
    <body style="font-family: Arial; padding: 40px; background: #0f172a; color: white;">
        <h2>Query:</h2>
        <p>{query}</p>

        <div class="card">
            <h3>Answer:</h3>
            <p>{data['answer']}</p>
        </div>

        <div class="card">
            <h3>Decision:</h3>
            <p class="{color_class}">{decision}</p>
        </div>

        <div class="card">
            <h3>Confidence Score:</h3>
            <p>{score}</p>
        </div>

        <div class="card">
            <h3>Context:</h3>
            <ul>
                {''.join(f"<li>{c}</li>" for c in data['context'])}
            </ul>
        </div>

        <br><br>
        <a href="/">🔙 Ask another question</a>
    </body>
    </html>
    """