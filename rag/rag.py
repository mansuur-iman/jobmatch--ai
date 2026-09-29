from retrieval.retriever import retriever
from generator.generator import generate_response
def run_rag(job_description:str)->str:
    try:
        context = retriever(job_description)
        if not context.strip():
            return "No candidate data found for this job."
        response = generate_response(
            job_description,
            context
        )
        return response
    except Exception as e:
        print(f"error in rag: {e}")
        return ""