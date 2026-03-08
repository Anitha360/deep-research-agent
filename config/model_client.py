from autogen_ext.models.openai import OpenAIChatCompletionClient


def get_model_client():

    return OpenAIChatCompletionClient(
        model="qwen2.5:7b",
        base_url="http://localhost:11434/v1",
        api_key="ollama",

        model_info={
            "vision": False,
            "function_calling": True,
            "json_output": True,
            "structured_output": False,
            "family": "qwen",
        },

        temperature=0.7,
    )