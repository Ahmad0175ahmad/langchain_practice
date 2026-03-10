from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import ChatOpenAI

text ="""Logic ke lihaaz se (Aasan hai): Ek basic bot banana jo page refresh kare aur button click kare, kisi bhi average Python developer ke liye aasan kaam hai.

Real-world Challenges (Thoda mushkil ho sakta hai): 1.  Bot Detection: Amazon ya aise bare portals ke paas strict anti-bot systems (jaise Cloudflare, reCAPTCHA) hote hain. "Human-like browser interaction" achieve karna aur block hone se bachna is project ka sab se mushkil hissa ho sakta hai.
2.  Dynamic Web Pages: Agar website ka structure bar bar change hota hai, toh script break ho sakti hai aur aapko code update karna parega.

"""

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)
result =splitter.split_text(text)
print(result)