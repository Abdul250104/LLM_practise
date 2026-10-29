from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
import os
load_dotenv()
llm = ChatGoogleGenerativeAI( model="gemini-2.5-flash",google_api_key=os.getenv("GEMINI_API_KEY") )
# st.title("ai agent call")
# query = st.chat_input("enter the message")
# if query:
#     st.chat_message("user").markdown(query)
#     response=llm.invoke(query)
#     st.chat_message("ai").markdown(response.content)
history =[]
while True:
    que=input("user: ")
    history.append({"role":"user","content":que})
    if que.lower() in ["exit","back"]:
        print("thank you")
        break
    response= llm.invoke(history)
    history.append({"role":"ai","content":response.content})
    print("AI: ",response.content)