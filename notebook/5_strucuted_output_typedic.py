from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
from typing import TypedDict , Optional,Annotated,Literal
from pydantic import BaseModel,Field
import os

load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key = os.getenv("GOOGLE_API_KEY")
)

class review(BaseModel):
    key:list[str] = Field(deprecated="key components")
    sentiment:Annotated[Literal["pos","neg"],"return setimnent of porduct"]
    summery:str
    rating:str

structe_model = model.with_structured_output(review) 
# with_structure_output
response = structe_model.invoke("I recently purchased these wireless headphones and I’m really impressed with the sound quality. The battery lasts a long time and they are comfortable to wear. However, the microphone quality could be better. Overall, it’s a good product for the price, and I would recommend it.")
print(response)