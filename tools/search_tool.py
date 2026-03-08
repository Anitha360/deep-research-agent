from ddgs import DDGS
from typing import List, Dict

def search_web(query: str) -> List[Dict]:
    results = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=5):
            results.append({
                "title": r["title"],
                "link": r["href"],
                "snippet": r["body"]
            })

    return results