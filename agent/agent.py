import json

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

from schemas.match import JobMatchOutput

load_dotenv()

SYSTEM_PROMPT = """
You are a job matching assistant.

You will be given a candidate profile and a job description.

Match the candidate profile against the job using ONLY the information
provided in the profile and job.

You must:

1. Identify matching requirements.
2. Identify missing requirements.
3. Identify important gaps.
4. Explain why the profile matches or does not match the job.

Do not use external knowledge.
Do not assume information that is not provided.
"""

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
structured_llm = llm.with_structured_output(JobMatchOutput)


async def match_profile_to_job(profile: dict, job: str) -> dict:
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(
            content=f"Candidate profile:\n{json.dumps(profile)}\n\nJob:\n{job}"
        ),
    ]
    result = await structured_llm.ainvoke(messages)
    return result.model_dump()