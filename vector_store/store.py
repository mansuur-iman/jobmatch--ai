import os
from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_postgres import PGVector

load_dotenv()

def get_vector_store():
    try:
        db_connection = os.environ.get("DATABASE_URL")
        embeddings_model = GoogleGenerativeAIEmbeddings(model="gemini-embeddings-2")

        vector_store = PGVector(connection=db_connection, embeddings=embeddings_model, collection_name="collection1")
        return vector_store
    except Exception as e:
        print(f"error in storing vector: {e}")