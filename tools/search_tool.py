from ddgs import DDGS
from typing import List, Dict
from config.logger import get_logger

logger = get_logger("Web Search")

def search_web(query: str) -> List[Dict]:
    results = []
    logger.info("Initializing Web search")
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=5):
            results.append({
                "title": r["title"],
                "link": r["href"],
                "snippet": r["body"]
            })
    logger.info("Web search Successfully completed")
    return results