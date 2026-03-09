from autogen_agentchat.agents import AssistantAgent
from config.model_client import get_model_client

from tools.search_tool import search_web
from tools.web_scraper import scrape_page
from config.logger import get_logger

logger = get_logger("Researcher")

def create_researcher():
    logger.info("Initializing Research")
    researcher = AssistantAgent(
        name="researcher",
        model_client=get_model_client(),
        tools=[search_web, scrape_page],
        system_message="""
You are a research expert.

Steps:
1. Search the web for information
2. Open relevant pages
3. Extract important content
4. Summarize findings
"""
    )
    logger.info("research work completed")
    return researcher
