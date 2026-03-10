from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

document =[
    "Islamabad is the capital of Pakistan",
    "Karachi is the city of lights",
    "Hockey is national game of Pakistan"
]
embeddings =OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)
result =embeddings.embed_documents(document)
print(str(result))

