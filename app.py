import streamlit as st
import numpy as np
import requests
import pickle
import joblib

model_path = "saved_steps.pkl"
model = joblib.load(model_path)

# Streamlit app
st.title("Prediction of Cannula Distorted")
