from autogen_agentchat.agents import AssistantAgent
from config.model_client import get_model_client


def create_writer():

    writer = AssistantAgent(
        name="writer",
        model_client=get_model_client(),
        system_message="""
You are a professional report writer.

Combine all findings and produce a structured research report:

1. Introduction
2. Key Findings
3. Analysis
4. Conclusion
"""
    )

    return writer