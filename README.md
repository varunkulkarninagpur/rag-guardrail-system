# 🔥 RAG Guardrail System (Hallucination Detection)

## 🚀 Overview

A production-style Retrieval-Augmented Generation (RAG) system with a **verification layer** that detects and filters hallucinated responses from LLMs.

---

## 🎯 Problem

Traditional RAG systems:

* Retrieve incorrect context
* Generate hallucinated answers
* Lack trust and reliability

---

## 💡 Solution

This system introduces a **verification layer** that:

* Checks semantic alignment
* Measures keyword overlap
* Assigns confidence score
* Rejects low-confidence answers

---

## 🧠 Architecture

User Query → Retrieval → Generation → Verification → Final Decision

---

## ⚙️ Tech Stack

* FastAPI (Microservices)
* FAISS (Vector DB)
* SentenceTransformers (Embeddings)
* Transformers (LLM)
* Python

---

## 🔧 Services

### 1. Retrieval Service (Port 8001)

* Document chunking
* Embedding generation
* FAISS similarity search

### 2. Generation Service (Port 8002)

* LLM-based answer generation
* Prompt engineering

### 3. Verification Service (Port 8003)

* Semantic similarity scoring
* Keyword overlap scoring
* Final confidence score

### 4. Query Service (Port 8004)

* Orchestrates full pipeline
* Applies decision logic

### 5. UI Service (Port 8005)

* User-friendly interface
* Displays answer + confidence

---

## 🔥 Features

* Microservices architecture
* Hallucination detection
* Confidence scoring
* Real-time verification
* Interactive UI

---

## 🧪 Example

Query: What is AI?

Output:

* Answer: Generated response
* Confidence: 0.91
* Decision: ACCEPTED

---

## 🚀 Future Improvements

* Replace GPT2 with Mistral / LLaMA
* Add feedback learning
* Deploy using Docker & Kubernetes
* Improve UI with React

---

## 🧠 Learnings

* RAG pipelines
* Vector databases
* Microservices communication
* AI reliability systems

---

## 👨‍💻 Author

Varun Kulkarni
