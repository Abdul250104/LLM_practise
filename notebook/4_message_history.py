import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from IPython.display import display, Markdown

# Environment variables load karein
load_dotenv()

# Model initialize karein
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")   
)

message_history =[]

while True:
    query = input("user :")
    message_history.append({"role":"user",
                            "content":query})
    if query.lower() in ['exit']:
        break
    respose=llm.invoke(message_history)
    message_history.append({"role":"ai",
                            "content":respose.content})
    print("ai: ")
    print(display(Markdown(respose.content)))