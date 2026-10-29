from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
loader = TextLoader('palastine.txt')
docs=loader.load()
prompt = PromptTemplate(
    template='you are explain this is right or not your answer only yes and no  {topic}',
    input_variables=['topic',]
)
parser = StrOutputParser()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key = os.getenv("GOOGLE_API_KEY")
)

chain = prompt | model | parser

print(chain.invoke({"topic":" Palestinian society not diverse."}))
