from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt
load_dotenv()
model =ChatOpenAI(model='gpt-4')

st.header("Research Tool")
# user_input=st.text_input("Enter your Prompt")

paper_input =st.selectbox("Select Research Paper Name ", ["Select...", "Attention is all you need",
    "BERT: Pre-training of Deep Bidirectional Transformer", "GPT-3: Language Models are Few-Shot Learners",
    "Diffusion Models Beat GANs on Image Synthesis"])

style_input =st.selectbox("Select Explanaiton Style ", ["Beginner-Friendly", "Technical", "Code-oriented",
    "Mathematical"])

lenght_input=st.selectbox("Select Explanation Length ", ["short (1-2 paragraphs)",
    "Medium (3-5 paragraphs)", "Long (detailed Explanation)"])

template= load_prompt("template.json")




if st.button("Summarize"):
   chain = template | model
   result=chain.invoke(   {
      'paper_input':paper_input,
      'style_input':style_input,
      'length_input':lenght_input
   })
   st.write(result.content)

