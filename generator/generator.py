from langchain_google_genai import ChatGoogleGenerativeAI

SYSTEMP_PROMPT = """
You are a job matching assitant.
You will be given a candidate details and a job description.
You are required to analyze the candidate's details against a job description.

JOB DESCRIPTION:
{job_description}

CANDIDATE DETAILS:
{candidate_details}

Based on only the candiadte detail provided:
1.identify matching skills and experience.
2.identify missing requirements.
3.maintain relevant projects.
4.explain any important gaps.

DO NOT INVENT CANDIDATE EXPERIENCE OR REQUIREMENT THAT IS NOT IN THE EVIDENCE.
"""

llm_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

def generate_response(job_description:str, context:str)-> str:
    try:
        prompt = SYSTEMP_PROMPT.format(job_description=job_description, candidate_details=context)
        response = llm_model.invoke(prompt)
        content = response.content
        return content
    except Exception as e:
        print(f"error: {e}")
        return ""