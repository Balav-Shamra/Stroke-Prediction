import streamlit as st
from PIL import Image
import pandas as pd
import pickle

st.set_page_config(
    page_title="Stroke Predictor",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown("<h1 style='color:grey;font-weight:bold;text-align:center;padding-bottom:20px;margin-top:-20px'>Empowering the World of Prediction</h1>",
                unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    img = Image.open("doctor_instrument.jpeg")
    st.image(img, use_column_width="always")
    st.markdown("<p style='color:grey;font-weight:bold;'> The system utilizes medical records of a patients to determine the presence or absence of stroke.</p>",
                 unsafe_allow_html=True)

with col2:
    img = Image.open("about_us.jpeg")
    st.image(img, use_column_width="always")

    st.markdown("<h1 style='color:green;font-weight:bold;text-shadow: 1px 2px 1px #000F00;'>Stroke Prediction</h1>"
                "<h4 style='color:grey;text-align:center;font-weight:bold;'>Machine Learning</h4>",
                unsafe_allow_html=True)

st.markdown("<hr style='border: 1px dotted grey;'>",
            unsafe_allow_html=True)

st.markdown("<h6 style='text-align:center;font-weight:bold;color:grey;margin-top:-6px;'>Aims to predict Stroke status of the Patient.</h6>",
            unsafe_allow_html=True)

st.markdown("<hr style='border: 1px dotted grey;margin-top:4px;'>",
            unsafe_allow_html=True)




