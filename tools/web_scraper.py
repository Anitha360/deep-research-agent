import requests
from bs4 import BeautifulSoup
from config.logger import get_logger

logger = get_logger("Web Scarper")

def scrape_page(url: str):

    try:
        logger.info("Initializing web scraper")
        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")

        text = " ".join(p.get_text() for p in paragraphs)
        logger.info("Web scraper completed")
        return text[:3000]

    except Exception as e:

        return f"Scraping error: {e}"