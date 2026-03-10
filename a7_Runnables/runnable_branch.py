from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableBranch, RunnableSequence, RunnablePassthrough
from langchain_core.prompts import PromptTemplate
load_dotenv()

model=ChatOpenAI()

parser=StrOutputParser()

prompt1=PromptTemplate(
    template='write a detailed note on {topic}',
    input_variables=['topic']
)

promp2=PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)

report_generation_chain =RunnableSequence(prompt1,model, parser)

branch_chain =RunnableBranch(
    (lambda x:len(x.split())>500, RunnableSequence(promp2, model, parser)),
    RunnablePassthrough()
)

final_chain =RunnableSequence(report_generation_chain, branch_chain)
print(final_chain.invoke({'topic':'ukraine vs russia'}))