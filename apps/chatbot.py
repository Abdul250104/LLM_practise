from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os




load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key = os.getenv("GOOGLE_API_KEY")
)

while True:
    query = input("")
    if query in ['exit']:
        break
    response = model.invoke(query)
    print(response)