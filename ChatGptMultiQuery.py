from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from ChatGptOpenAi import intital_respone_array, api_key
from AzureAiSearch import vector_store

def getDetails(response):
    docs = vector_store.similarity_search(
        query=response,
        k=5,
        search_type="similarity",
    )
    
    similar_content=[]
    for doc in docs:
        similar_content.append(doc.page_content)
    content = ''.join(similar_content)

    llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.5, api_key=api_key)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Assume that you are a highly qualified medical doctor with many years of academic and research experience. You specialization is in Respiratory and Pulmonary Medicine. Given reference content from a standard medical textbook, you are given the task of expanding it and giving detailed explanations. All the explanation from you should come from the specialization content reference matter provided here. Below is the specialization reference content :\n\n{content}\n\n. From the above specialization reference content provide detailed explaination for the below paragraph {response}.\n\n\n Give special focus on detailing any gentic related information. The answer should contain for 1000 words such that it scores maximum grade in a university examination.",
            )
        ]
    )

    chain = prompt | llm
    response = chain.invoke(
        {
            "content": content,
            "response": response
        }
    )

    return response.content

detailed_answer_array=[]
for response in intital_respone_array:
    detailed_answer_array.append(getDetails(response))