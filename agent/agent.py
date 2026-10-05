from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.graph import START, StateGraph, MessagesState
from schemas.match import JobMatchOutPut
from dotenv import load_dotenv
import json

load_dotenv()
    # build prompt
SYSTEM_PROMPT = """
You are a job matching agent.

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
Only use the provided profile and job data.
"""

llm  = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
structured_llm = llm.with_structured_output(JobMatchOutPut)

# call agent model with prompt
async def call_model(state:MessagesState)-> dict:
    #remove existing system message
    non_system_messages = [
        message for message in state["messages"] if not isinstance(message, SystemMessage)
    ]
    #create new system message
    messages = [SystemMessage(content=SYSTEM_PROMPT)] + non_system_messages
    #call model with system prompt
    response = await structured_llm.ainvoke(messages)

    return{
        "messages": [HumanMessage(content=response.model_dump_json(), name="agent_output")]
    }
#Build the agent graph
graph = StateGraph(MessagesState)
graph.add_node("agent", call_model)

graph.add_edge(START, "agent")
app = graph.compile()

async def match_agent(profile:dict, job:str)-> dict:
 message = HumanMessage(content=f"""candidate profile: {profile} job: {job}""")

 result = await app.ainvoke({"messages" : [message]})
 content = result["messages"][-1].content
 structured_data = json.loads(content)

 return structured_data