from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel
from typing import Literal
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


# Output structure
class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"]


parser = PydanticOutputParser(pydantic_object=Feedback)
str_parser = StrOutputParser()


# Classifier prompt
prompt1 = PromptTemplate(
    template="""Classify the sentiment of the following feedback
as either positive or negative.

Feedback: {feedback}

{format_instruction}
""",
    input_variables=["feedback"],
    partial_variables={
        "format_instruction": parser.get_format_instructions()
    }
)


# Positive response
prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback: {text}",
    input_variables=["text"]
)


# Negative response
prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback: {text}",
    input_variables=["text"]
)


# Branch
branch_chain = RunnableBranch(
    (
        lambda x: x.sentiment == "positive",
        prompt2 | model | str_parser
    ),
    (
        lambda x: x.sentiment == "negative",
        prompt3 | model | str_parser
    ),
    RunnableLambda(lambda x: "Could not get review")
)


# IMPORTANT: use Pydantic parser here
classifier_chain = prompt1 | model | parser

final_chain = classifier_chain | branch_chain


response = final_chain.invoke({
    "feedback": "that smartphone is not best"
})

print(response)

