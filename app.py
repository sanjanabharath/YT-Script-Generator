import os
from apikey import apikey
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

os.environ['OPENAI_API_KEY'] = apikey

st.title('🦜🔗 YouTube GPT')
prompt = st.text_input('Plug in your prompt here')

title_template = PromptTemplate(
    input_variables = ['topic'],
    template = 'Write me a youtube video title about {topic}'
)

script_template = PromptTemplate(
    input_variables = ['title'],
    template = 'Write me a youtube video script for the title {title}'
)

llm = OpenAI(temperature=0.8)
title_chain = LLMChain(llm=llm, prompt=title_template)
script_chain = LLMChain(llm=llm, prompt=script_template)
sequential_chain = SimpleSequentialChain(chains=[title_chain, script_chain])

if prompt:
    response = sequential_chain.run(prompt)
    st.write(response)