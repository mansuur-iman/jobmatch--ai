from rag.rag import run_rag
def main():
     job_description = "Ai engineer who can build ai systems end to end with also a knowledge of sofware engineering (backend and frontend). we use python for the ai system so the engineer should be able to use python idependently with its tools like langchain. you should have an education in bachelor of computer science, it and any other related field."
     result = run_rag(job_description)
     print(result)
if __name__ == "__main__":
    main()