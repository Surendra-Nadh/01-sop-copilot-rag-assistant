"""Lightweight evaluation (RAGAS-style) for SOP Copilot.
Run: python src/evaluate.py
Output: evaluation_results.csv

Metrics:
- Context Relevance: % of retrieved chunks that share keywords with question (proxy for context_precision)
- Answer Relevance: overlap between answer and expected keywords (proxy)
- Citation Coverage: has sources? (1 if yes)

For strict RAGAS, install ragas + OpenAI key and run answer_relevancy / context_precision.
"""
import csv

from src.retrieve import answer

TEST_QA = [
    ("What is password reset procedure?", ["password", "reset", "90 days"]),
    ("What is refund policy?", ["refund", "30 days"]),
    ("What is leave policy?", ["leave", "24"]),
    ("What is incident response SLA?", ["incident", "15 minutes"]),
    ("What is data retention period?", ["retention", "90 days"]),
    ("What is vendor onboarding?", ["vendor", "KYC"]),
    ("What is travel policy hotel cap?", ["travel", "7500"]),
    ("What is backup procedure?", ["backup", "daily", "2AM"]),
    ("What is audit trail?", ["audit", "quarterly"]),
    ("What is change management window?", ["change", "Sunday"]),
]

def eval_one(q, expected_keywords):
    res = answer(q)
    ans_lower = res["answer"].lower()
    # Answer relevance: % keywords found
    hits = sum(1 for k in expected_keywords if k in ans_lower)
    ans_rel = hits / len(expected_keywords) if expected_keywords else 0
    # Context relevance: sources present and answer not "Not found"
    ctx_score = 1.0 if res["sources"] and "not found" not in ans_lower else 0.0
    citation = 1.0 if res["sources"] else 0.0
    return ans_rel, ctx_score, citation, res["answer"], ", ".join(res["sources"])

def main():
    rows = []
    tot_ans, tot_ctx, tot_cit = 0, 0, 0
    print("Evaluating 10 QA pairs ...")
    for q, kw in TEST_QA:
        a, c, cit, ans, src = eval_one(q, kw)
        print(f"Q: {q}\n  ans_rel={a:.2f} ctx={c:.2f} cit={cit:.2f} -> {ans[:90]}...")
        rows.append([q, a, c, cit, ans, src])
        tot_ans += a; tot_ctx += c; tot_cit += cit

    n = len(TEST_QA)
    print(f"\n=== RESULTS ===")
    print(f"Avg Answer Relevance : {tot_ans/n:.3f}")
    print(f"Avg Context Precision: {tot_ctx/n:.3f}")
    print(f"Citation Coverage    : {tot_cit/n:.3f}")

    with open("evaluation_results.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["question", "answer_relevance", "context_precision", "citation_coverage", "answer", "sources"])
        w.writerows(rows)
    print("Saved evaluation_results.csv")

if __name__ == "__main__":
    main()
