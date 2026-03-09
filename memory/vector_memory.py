import chromadb
from config.logger import get_logger

logger = get_logger("Vector Memory")
client = chromadb.Client()

collection = client.create_collection("research_memory")


def store_memory(text):
    logger.info("Memory Store")
    collection.add(
        documents=[text],
        ids=[str(hash(text))]
    )


def retrieve_memory(query):
    logger.info("Memory Retriever")
    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    return results