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




st.markdown("<h1 style='color:black;text-align:center;font-weight:bold;'>Stroke Prediction</h1>",
            unsafe_allow_html=True)


df = pd.read_csv("CleanedStrokeData.csv")

st.markdown("<h6 style='color:black;font-weight:bold;text-align:center;padding:20px;'>Enter Patient Details</h6>",
            unsafe_allow_html=True)


with st.form("form"):

    gender = st.selectbox("Gender", options=df["gender"].unique(), label_visibility="visible")

    age = st.slider("Enter Age:", min_value=1, max_value=int(df["age"].max()), step=1, label_visibility="visible")

    c1, c2, c3 = st.columns(3)
    with c1:
        ever_married = st.radio("Are you Married:", options=df["ever_married"].unique(), label_visibility="visible")

    with c2:
        heart_disease = st.radio("Heart Disease:", options=["Yes", "No"])

    with c3:
        hyper_tension = st.radio("Hypertension:", options=["Yes", "No"])

    avg_glucose_level = st.number_input("Glucose Level:", min_value=0.0, max_value=df["avg_glucose_level"].max())

    residence_type = st.selectbox("Residence Type:", options=df["Residence_type"].unique())

    smoking_status = st.selectbox("Smoking Status:", options=df["smoking_status"].unique())

    work_type = st.selectbox("Work Type:", options=df["work_type"].unique())

    if hyper_tension == "Yes":
        hyper_tension = 1
    elif hyper_tension == "No":
        hyper_tension = 0

    if heart_disease == "Yes":
        heart_disease = 1
    elif heart_disease == "No":
        heart_disease = 0

    s1, s2, s3 = st.columns((2.1, 2, 1))
    with s2:
        st.form_submit_button("Diagonise")

inputs = pd.DataFrame({"hypertension":[hyper_tension], "heart_disease": [heart_disease], "ever_married":[ever_married], "Residence_type":[residence_type],
                       "smoking_status":[smoking_status], "avg_glucose_level":[avg_glucose_level], "work_type":[work_type], "age":[age], "gender":[gender]})

with st.expander("See User Inputs:", expanded=False):
    ex1, ex2, ex3 = st.columns(3)
    with ex2:
        for col in inputs.columns:
            if inputs[col][0] == 1:
                st.write(f"{col} - **Yes**")

            elif inputs[col][0] == 0:
                st.write(f"{col} - **No**")

            else:
                st.write(f"{col} - **{inputs[col][0]}**")


svm_model = pickle.load(open("svm_Stroke_predictor.pickle", "rb"))
y_pred = svm_model.predict(inputs)

if y_pred[0] == 0:
    st.write('<h3 style="color:blue; text-align:center;">No Stroke Detected</h3>',
    unsafe_allow_html=True)
else:
    st.write('<h3 style="color:red; text-align:center;">Stroke Detected</h3>',
             unsafe_allow_html=True)



