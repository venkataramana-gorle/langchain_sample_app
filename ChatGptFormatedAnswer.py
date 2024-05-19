from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from ChatGptMultiQuery import detailed_answer_array, api_key, vector_store

def format_answer(answer):
    docs = vector_store.similarity_search(
        query="graphs names and table names for "+answer,
        k=3,
        search_type="similarity",
    )
    
    relevant_tables_graphs=[]
    for doc in docs:
        relevant_tables_graphs.append(doc.page_content)
    relevant_tables_graphs_content = ''.join(relevant_tables_graphs)

    llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0, api_key=api_key)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Assume that you are a highly qualified medical doctor with many years of academic and research experience. You specialization is in Respiratory and Pulmonary Medicine. Your task is to format the content provided below as per university level post graduate examination standards. Below is the content:\n\n----------------\n\n{answer}\n\n-----------------------\n\n Please insert a annotation specifying the name of a relevant graph or table which will enhance the quality and understanding of the above content from the text provided below.\n\n-------------------------\n\n{relevant_tables_graphs_content}",
            )
        ]
    )

    chain = prompt | llm
    response = chain.invoke(
        {
            "answer": answer,
            "relevant_tables_graphs_content": relevant_tables_graphs_content
        }
    )

    return response.content

final_answer_array=[]
for deatiled_answer in detailed_answer_array:
    final_answer_array.append(format_answer(deatiled_answer))

print(''.join(final_answer_array))