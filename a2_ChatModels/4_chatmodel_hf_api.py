from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    max_new_tokens=50,
)

model =ChatHuggingFace(llm=llm)
result =model.invoke("what is the capital of pakistan?")
print(result.content)