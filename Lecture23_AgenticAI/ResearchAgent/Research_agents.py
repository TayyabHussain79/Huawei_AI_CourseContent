import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import Tool
from langchain.agents import create_react_agent
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import AgentExecutor

# -------------------------------
# 1. Load API keys from .env
# -------------------------------
load_dotenv()

GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

# -------------------------------
# 2. Initialize Gemini LLM

# -------------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0.3
)

# -------------------------------
# 3. Define Tools
# -------------------------------
search = SerpAPIWrapper()

search_tool = Tool(
    name="Web Search",
    func=search.run,
    description="Useful for retrieving live information from the web"
)

# -------------------------------
# 4. Build Agent (new way)
# -------------------------------
from langchain import hub
prompt = hub.pull("hwchase17/react")  # standard ReAct prompt

agent = create_react_agent(llm=llm, tools=[search_tool], prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=[search_tool], verbose=True)

# -------------------------------
# 5. Run Research Query
# -------------------------------
def research_query(query: str):
    print("\n🔎 Research Query:", query)
    response = agent_executor.invoke({"input": query})
    print("\n📌 Research Assistant Answer:\n", response["output"])

if __name__ == "__main__":
    research_query("Summarize the latest research on AI agents in 2025.")