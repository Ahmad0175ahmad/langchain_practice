from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter =SemanticChunker(
    OpenAIEmbeddings(), breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)



sample ="""
A farmer is the backbone of human civilization. They are the dedicated individuals who cultivate the land, raise livestock, and provide the world with the food and raw materials necessary for survival. Whether they are growing grains like wheat and rice or managing dairy farms, their work is a blend of traditional knowledge and modern science.
The life of a farmer is defined by the rhythms of nature. A typical day often begins before sunrise, tending to animals or preparing the fields while the air is still cool. Their work is physically demanding and requires a diverse set of skills—they must be part mechanic (to fix tractors), part scientist (to understand soil nutrients), and part weather forecaster.
"""

docs =text_splitter.create_documents([sample])

print(len(docs))
print(docs)
