import faiss
import numpy as np
import os
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STORE_DIR = os.path.abspath(os.path.join(BASE_DIR, "../../data/vector_store"))

# Ensure directory exists
os.makedirs(STORE_DIR, exist_ok=True)

INDEX_PATH = os.path.join(STORE_DIR, "faiss.index")
DOC_PATH = os.path.join(STORE_DIR, "docs.pkl")

dimension = 384  # embedding size

# Initialize FAISS index
if os.path.exists(INDEX_PATH):
    index = faiss.read_index(INDEX_PATH)
    with open(DOC_PATH, "rb") as f:
        documents = pickle.load(f)
else:
    index = faiss.IndexFlatL2(dimension)
    documents = []


def add_embeddings(embeddings, texts):
    global documents
    
    vectors = np.array(embeddings).astype("float32")
    index.add(vectors)
    documents.extend(texts)

    faiss.write_index(index, INDEX_PATH)
    with open(DOC_PATH, "wb") as f:
        pickle.dump(documents, f)


def search(query_embedding, top_k=5):
    vector = np.array([query_embedding]).astype("float32")
    distances, indices = index.search(vector, top_k)

    results = []
    for idx in indices[0]:
        if idx < len(documents):
            results.append(documents[idx])
    
    return results