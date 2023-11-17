"""
Langchain is a popular library in natural language processing (NLP) wrapped around a Large Language Model (LLM).

Langchain can work with pgvector to store and query embeddings to add context during prompt engineering.


- https://python.langchain.com/docs/integrations/vectorstores/pgvector

"""
import os
from langchain.docstore.document import Document
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.pgvector import PGVector
from langchain.embeddings import HuggingFaceEmbeddings


CONNECTION_STRING = PGVector.connection_string_from_db_params(
    driver=os.environ.get("PGVECTOR_DRIVER", "psycopg"),
    host=os.environ.get("PGVECTOR_HOST", "localhost"),
    port=int(os.environ.get("PGVECTOR_PORT", "5432")),
    database=os.environ.get("PGVECTOR_DATABASE", "vector"),
    user=os.environ.get("POSTGRES_USER", "postgres"),
    password=os.environ.get("POSTGRES_PASSWORD", "postgres"),
)

COLLECTION_NAME = "EWD_trip_report_US_UK"

loader = TextLoader("/workspace/data/EWD_trip_report.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# Specify the path to the pre-trained model
modelPath = "BAAI/bge-large-en-v1.5"
# Create a dictionary with model configuration options, specifying to use the CPU for computations
model_kwargs = {"device": "cpu"}
# Initialize an instance of HuggingFaceEmbeddings with the specified parameters
embeddings = HuggingFaceEmbeddings(
    model_name=modelPath,  # Provide the pre-trained model's path
    model_kwargs=model_kwargs,  # Pass the model configuration options
)

# initialize langchain pgvector wrapper and provide documents and embedding model
db = PGVector.from_documents(
    embedding=embeddings,
    documents=docs,
    collection_name=COLLECTION_NAME,
    connection_string=CONNECTION_STRING,
)


# Using a VectorStore as a Retriever
retriever = db.as_retriever()

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough

template = """Answer the question based only on the following context:

{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
model = ChatOpenAI(model_name="gpt-3.5-turbo")


def format_docs(docs):
    return "\n\n".join([d.page_content for d in docs])


chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

answer = chain.invoke("What did edgar say about take off from schiphol?")

print(answer)
