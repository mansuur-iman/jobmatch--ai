from vector_store.store import get_vector_store
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

vector_store = get_vector_store()


def process_documents(documents):
    try:
        langchain_documents = []

        for document in documents:
            langchain_document = Document(
                page_content=document["content"],
                metadata={
                    "source": document["source"]
                }
            )

            langchain_documents.append(langchain_document)

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )

        chunks = text_splitter.split_documents(langchain_documents)

        vector_store.add_documents(chunks)

        print(f"Successfully chunked and stored {len(chunks)} chunks")

        return chunks

    except Exception as e:
        print(f"Failed to process and store chunks: {e}")
        return []
