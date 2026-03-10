from langchain_huggingface import HuggingFaceEmbeddings

embedding =HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

text= "pakistan is the most beautiful city"

vector =embedding.embed_query(text)
print(str(vector))