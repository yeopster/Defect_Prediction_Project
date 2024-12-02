import streamlit as st
import numpy as np
import requests
import pickle

with open('saved_steps.pkl', 'rb') as file:
  model = pickle.load(file)
# Streamlit app
st.title("Prediction of Cannula Distorted")
