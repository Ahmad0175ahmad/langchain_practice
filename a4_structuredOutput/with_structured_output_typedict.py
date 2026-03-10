from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

model=ChatOpenAI()
#schema
class Review(TypedDict):
    summary:Annotated[str,"A brief summary of the review"]
    sentiment:Annotated[str,"Return sentiment of the review either negative, positive or neutral"]

structured_output =model.with_structured_output(Review)

result =structured_output.invoke("""The hardware is great, but the software feels bloated. Their are to many pre-installed
    apps that i can't remove. Also, the UI looks outdated compared to other brands. Hoping for a 
    software update to fix this. 
    """)

print(result)
print(result['summary'])
print(result['sentiment'])

