from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

result =model.invoke("what is the capital of pakistan?")
print(result.content)







# from google import genai
# import os
# from dotenv import load_dotenv

# load_dotenv()
# api_key = os.getenv("GOOGLE_API_KEY")

# client = genai.Client(api_key=api_key)

# # List available models
# models = client.models.list()  # <- correct method
# for m in models:
#     print(m.name, m.supported_actions)