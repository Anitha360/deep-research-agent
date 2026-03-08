from autogen_agentchat.agents import AssistantAgent
from config.model_client import get_model_client


def create_critic():

    critic = AssistantAgent(
        name="critic",
        model_client=get_model_client(),
        system_message="""
You review the research.

Check:
- missing information
- weak arguments
- research quality
"""
    )

    return critic