from autogen_agentchat.agents import AssistantAgent
from config.model_client import get_model_client


def create_planner():

    planner = AssistantAgent(
        name="planner",
        model_client=get_model_client(),
        system_message="""
You are a research planner.

Break the research problem into structured tasks.
Create a research plan and key questions.
"""
    )

    return planner