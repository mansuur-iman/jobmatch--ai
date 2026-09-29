from vector_store.store import get_vector_store

vector_store = get_vector_store()
def retriever(job_description:str)-> str:
    try:
        results = vector_store.similarity_search(job_description, k=5)

        if not results:
            return f"No matching documents."

        context = ""

        for result in results:
            context += result.page_content + "\n"
        return context
    except Exception as e:
        print(f"Error in searching similarity: {e}")
        
