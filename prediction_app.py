# -*- coding: utf-8 -*-
"""prediction_app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19X1cg0LpDIE8RLkOiUy-2gLVWuFQuASd
"""

pip install streamlit

import streamlit as st
import numpy as np
import pickle

with open('model_prediction_rf.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Prediction of Cannula Distorted")

drawing = st.number_input("Drawing", min_value=0.0, format="%.2f")
bright_annealing = st.number_input("Bright Annealing", min_value=0.0, format="%.2f")
sinking = st.number_input("Sinking", min_value=0.0, format="%.2f")
electro_fission = st.number_input("Electro Fission", min_value=0.0, format="%.2f")

if st.button("Predict"):

    input_features = np.array([[drawing, bright_annealing, sinking, electro_fission]])

    prediction = model.predict(input_features)[0]

    if prediction == 1:
       st.error("The Cannula is Distorted: Defected")
    else:
       st.success("The Cannula is Not Distorted: No Defect")