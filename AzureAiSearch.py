import os

from langchain_community.vectorstores.azuresearch import AzureSearch
from langchain_openai import AzureOpenAIEmbeddings, OpenAIEmbeddings

# Option 1: use an OpenAI account
openai_api_key = os.getenv("openai_key")
openai_api_version: str = "2023-05-15"
model: str = "text-embedding-3-small"

vector_store_address: str = ""
vector_store_password: str = ""

embeddings: OpenAIEmbeddings = OpenAIEmbeddings(
    openai_api_key=openai_api_key, openai_api_version=openai_api_version, model=model
)

index_name: str = "langchain-sample-application"
vector_store = AzureSearch(
    azure_search_endpoint=vector_store_address,
    azure_search_key=vector_store_password,
    index_name=index_name,
    embedding_function=embeddings.embed_query,
)

