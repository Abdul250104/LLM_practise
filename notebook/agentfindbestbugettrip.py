import os 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_classic import hub
from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate
load_dotenv()
llm = ChatGoogleGenerativeAI(model ="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")   )

search_tool = DuckDuckGoSearchRun()



prompt = PromptTemplate.from_template("""
Answer the following question as best you can.

You have access to these tools:

{tools}

Use this format:

Question: the input question
Thought: consider what to do
Action: the action to take, must be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (repeat Thought/Action/Action Input/Observation if needed)
Thought: I now know the final answer
Final Answer: the final answer to the question

Begin!

Question: {input}
Thought:{agent_scratchpad}
""")

# 2. Create an agent

agent = create_react_agent(
    llm=llm,
    tools=[search_tool],
    prompt=prompt
)

# 3. Create the executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool],
    verbose=True
)

# 4. Run the agent
response = agent_executor.invoke({
    "input": "Search for budget trips to Goa"
})

print(response["output"])
