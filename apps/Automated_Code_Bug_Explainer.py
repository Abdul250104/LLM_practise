from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from IPython.display import display, Markdown
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
import os
import sys


load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key = os.getenv("GOOGLE_API_KEY")
)
prompt = PromptTemplate(
    template="""
    Read the following Python code and provide an analytical explanation.

    ```python
    {code}
    ```

    Explain:
    1. What the code does
    2. How it works
    3. Any errors
    4. Possible improvements
    """,
    input_variables=["code"]
)

parser = StrOutputParser()

chain = RunnableSequence(prompt, model, parser)
# Read multi-line code from standard input
print("Paste your Python code below (press Ctrl+D on Linux/Mac or Ctrl+Z on Windows + Enter to finish):")
code = sys.stdin.read().strip()

if code:
    # Bonus: streaming the output token-by-token directly in terminal
    for chunk in chain.stream({"code": code}):
        print(chunk, end="", flush=True)
    print()
else:
    print("No code was provided.")
# response=chain.invoke({"code":code})
# display(Markdown(response)) 