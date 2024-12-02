import streamlit as st
import numpy as np
import requests
import pickle

url = "https://github.com/yeopster/project/blob/main/saved_steps.pkl"

response = requests.get(url)

with open('saved_steps.pkl', 'wb') as file:
     file.write(response,content)

with open('saved_steps.pkl', 'rb') as file:
      model=pickel.load(file)

# Streamlit app
st.title("Prediction of Cannula Distorted")
