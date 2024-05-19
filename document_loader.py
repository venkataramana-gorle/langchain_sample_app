from langchain_community.document_loaders import PyPDFLoader
from AzureAiSearch import vector_store

# Replace with the actual path to your PDF file
pdf_path = "vectorstores/documents/fishman/Fishman-ch1-ch5.pdf"

# Initialize the loader
loader = PyPDFLoader(os.path.abspath(pdf_path))
chunks = []

for page in loader.lazy_load():
    chunks.append(page)

vector_store.add_documents(documents=chunks)