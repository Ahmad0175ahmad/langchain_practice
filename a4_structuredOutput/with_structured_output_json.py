from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field 
from typing import Literal,Optional,Annotated, TypedDict

load_dotenv()
model =ChatOpenAI()

#schema
json_schema={
    "title":"Review",
    "type":"object",
    "properties":{
        "summary":{
            "type":"string",
            "description":"A brief summary of the review"
        },
        "sentiment":{
            "type":"string",
            "enum":["pos","neg"],
            "description":"Return sentiment of the review either negative , positive or neutral"
        }
    },
    "required":["summary","sentiment"]
}

structured_output =model.with_structured_output(json_schema,method="function_calling")

result =structured_output.invoke("""The hardware is great, but the software feels bloated. Their are to many pre-installed
    apps that i can't remove. Also, the UI looks outdated compared to other brands. Hoping for a 
    software update to fix this. 
    """)

print(result)