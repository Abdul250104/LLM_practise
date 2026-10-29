from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")   
)
propmts=ChatPromptTemplate([
    ("system","you are a translator and tranlate input in {language}"),
    ("user"," {query}")

])
# final_prompt=propmts.format_messages({'language':'hindi','query':'i likes flowers'})
final_prompt = propmts.format_messages(
    language="Hindi",
    query="I love flowers"
)
response = llm.invoke(final_prompt)
print(response.content)