from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# ✅ Pydantic schema
class Person(BaseModel):
    name: str = Field(description="Name of the Person")
    age: int = Field(gt=18, description="Age of the Person")
    city: str = Field(description="City of the Person")

# ✅ parser
parser = PydanticOutputParser(pydantic_object=Person)

# ✅ PROMPT TEMPLATE (this was wrong before)
template = PromptTemplate(
    template="""
Generate the name, age and city of a fictional {place} person.

{format_instructions}
""",
    input_variables=["place"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    },
)

# ✅ chain
chain = template | model | parser

final_result = chain.invoke({"place": "Sri Lankan"})
print(final_result)