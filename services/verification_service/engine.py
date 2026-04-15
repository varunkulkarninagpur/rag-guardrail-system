from sentence_transformers import SentenceTransformer, util
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')


def semantic_score(answer, context_list):
    context_text = " ".join(context_list)

    emb1 = model.encode(answer, convert_to_tensor=True)
    emb2 = model.encode(context_text, convert_to_tensor=True)

    score = util.cos_sim(emb1, emb2).item()
    return score


def keyword_overlap(answer, context_list):
    answer_words = set(answer.lower().split())
    context_words = set(" ".join(context_list).lower().split())

    overlap = answer_words.intersection(context_words)

    if len(answer_words) == 0:
        return 0

    return len(overlap) / len(answer_words)


def verify_answer(answer, context):
    sem_score = semantic_score(answer, context)
    keyword_score = keyword_overlap(answer, context)

    final_score = (sem_score + keyword_score) / 2

    decision = "ACCEPTED" if final_score > 0.5 else "REJECTED"

    return {
        "semantic_score": round(sem_score, 3),
        "keyword_score": round(keyword_score, 3),
        "final_score": round(final_score, 3),
        "decision": decision
    }