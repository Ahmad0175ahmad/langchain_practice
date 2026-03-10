from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
prompt =PromptTemplate(
    template='Generate the summary of the following poem . \n {poem}',
    input_variables=['poem']
)
model=ChatOpenAI()
parser=StrOutputParser()
loader =TextLoader('cricket.txt', encoding='utf-8')

docs=loader.load()

chain = prompt | model | parser

result=chain.invoke({'poem':docs[0].page_content})
print(result)
# print(docs)

# print(type(docs))
# print(docs[0].page_content)
# print(docs[0].metadata)
