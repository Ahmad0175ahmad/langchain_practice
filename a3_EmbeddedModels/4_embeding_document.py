from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()

document =[
    "Babar Azam is one of the top-ranked batsmen in the world and has captained Pakistan in all formats of international cricket",
    "Shaheen Afridi is known for his fast bowling and ability to take early wickets with the new ball",
    "Mohammad Rizwan is a consistent wicketkeeper-batsman who has played many match-winning innings for Pakistan",
    "Wasim Akram is considered one of the greatest fast bowlers in cricket history",
    "Imran Khan led Pakistan to victory in the 1992 Cricket World Cup"
]

query = "Who is Shaheen Afridi and what role has he played in the Pakistan cricket team?"

embedding= OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)
doc_embedding =embedding.embed_documents(document)
query_embedding =embedding.embed_query(query)


result = cosine_similarity([query_embedding], doc_embedding)[0]
index, score =sorted(list(enumerate(result)), key =lambda x:x[1])[-1]

print(query)
print(document[index])
print("Similarity Score is : ",score)