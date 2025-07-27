# it can be my app

import requests
import streamlit as st

def get_geminiai1_response(inp_text):
    response= requests.post("http://localhost:8000/essay/invoke",
    json={'input': {'topic': inp_text}})
    return response.json()['output']['content']

def get_geminiai2_response(inp_text):
    response= requests.post("http://localhost:8000/poem/invoke",
    json={'input': {'topic': inp_text}})
    return response.json()['output']['content']


st.title("Langchain Demo 2 models")
input_text= st.text_input("Write a essay on")
input_text1= st.text_input("Write a poem on")

if input_text:
    st.write(get_geminiai1_response(input_text))


if input_text1:
    st.write(get_geminiai2_response(input_text1))