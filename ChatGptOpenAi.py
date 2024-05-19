import os

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from AzureAiSearch import vector_store

api_key=os.getenv("api_key")

question="Describe about Pulmonary Surfactant and Disorders of Surfactant Homeostasis"

# Perform a similarity search
docs = vector_store.similarity_search(
    query=question,
    k=8,
    search_type="similarity",
)

similar_content=[]
for doc in docs:
    similar_content.append(doc.page_content)

content = ''.join(similar_content)

#print(content)

llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.3, api_key=api_key)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Assume that you are a highly qualified medical doctor with many years of academic and research experience. You specialization is in Respiratory and Pulmonary Medicine. Given the subject specialization content from a standard medical textbook, you are given the task of writing an ideal answer to the examination question asked by the a human student. The answer should contain for 1000 words such that it scores maximum grade in a university examination. All points should come from the specialization content reference matter provided below.Below is the attached subject matter specialization content:\n\n{content}\n\n",
        ),
        ("human", "{question}"),
    ]
)

chain = prompt | llm
response = chain.invoke(
    {
        "content": content,
        "question": question
    }
)

initial_response = response.content

intital_respone_array = list(filter(None,initial_response.splitlines()))