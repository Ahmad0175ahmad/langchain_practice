from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field 
from typing import Literal,Optional,Annotated, TypedDict

load_dotenv()
model =ChatOpenAI()

#schema 
class Review(BaseModel):
    summary: str =Field( description="A brief summary of the review")
    sentiment: Literal["pos","neg"] =Field( description="Return sentiment of the review either negative, positive or neutral")



structured_output =model.with_structured_output(Review,method="function_calling")

result =structured_output.invoke("""The hardware is great, but the software feels bloated. Their are to many pre-installed
    apps that i can't remove. Also, the UI looks outdated compared to other brands. Hoping for a 
    software update to fix this. 
    """)

print(result.summary)
print(result.sentiment)