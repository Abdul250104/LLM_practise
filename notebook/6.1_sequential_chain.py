from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

prompt1 = PromptTemplate(
    template='genrate 5 intresting fact about {topic}',
    input_variables=['topic',]
)

prompt2 = PromptTemplate(
    template=' this 5 fact convert into one line fact{fact}',
    input_variables=['fact',]
)
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key = os.getenv("GOOGLE_API_KEY")
)

parser = StrOutputParser()
chain = prompt1 | model | parser| prompt2 | model | parser
response = chain.invoke({'topic':'google'})
print(response)