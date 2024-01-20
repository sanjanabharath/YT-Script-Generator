import os
from apikey import apikey
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ['OPENAI_API_KEY'] = apikey

st.title('🦜🔗 YouTube GPT')
prompt = st.text_input('Plug in your prompt here')

title_template = PromptTemplate(
    input_variables = ['topic'],
    template = 'Write me a youtube video title about {topic}'
)

llm = OpenAI(temperature=0.8)
title_chain = LLMChain(llm=llm, prompt=title_template)

if prompt:
    response = title_chain.run(topic=prompt)
    st.write(response)