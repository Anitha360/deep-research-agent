from autogen_agentchat.agents import AssistantAgent
from config.model_client import get_model_client


def create_analyst():

    analyst = AssistantAgent(
        name="analyst",
        model_client=get_model_client(),
        system_message="""
You analyze research information.

Identify patterns, trends, and key insights.
"""
    )

    return analyst