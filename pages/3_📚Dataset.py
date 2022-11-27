import streamlit as st
import pandas as pd
from PIL import Image
import webbrowser

st.set_page_config(
    page_title="Dataset",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="expanded"
)
st.write("*****")
col1, col2 = st.columns((2))
st.write("*****")
with col1:
    st.markdown('<h1 style="color:#15b7e8;font-weight:bold;">Dataset</h1>',
                unsafe_allow_html=True)

    st.markdown('<h6 style="color:grey;">Stroke datasets for the project is downloaded from Kaggle.</h6>',
                unsafe_allow_html=True)

    # linking button to webpage
    url = "https://www.kaggle.com/"
    if st.button('Open Kaggle'):
        webbrowser.open_new_tab(url)



with col2:
    img = Image.open("datasets.png")
    st.image(img)

st.subheader("Display Dataset")
df = pd.read_csv("CleanedStrokeData.csv")
st.dataframe(df, use_container_width=False)  # same as st.write(df)

df = pd.read_csv("CleanedStrokeData.csv")

with st.expander("Data Description"):
    columns = ["gender","age","hypter_tension","heart_disease", "ever_married", "work_type",
               "Residence_type", "avg_glucose_level", "bmi", "smoking_status", "stroke"]

    t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11 = st.tabs(columns)
    with t1:
        st.write("Male or Female")

    with t2:
        st.write("Age of a Patient")

    with t3:
        st.write("1 if the patient has hypter tension, else 0")

    with t4:
        st.write("1 if the patient has heart disease, else 0")

    with t5:
        st.write("Yes or No")

    with t6:
        st.write("Government Job, Private Job or Self Emplpoyed")

    with t7:
        st.write("Rural or Urban")

    with t8:
        st.write("Average Glucose level in blood")

    with t9:
        st.write("Body Mass Index")

    with t10:
        st.write("Formerly Smoked, Never Smoked or Smokes currently")

    with t11:
        st.write("1 if the patient has Stroke, else 0")

with st.expander("Dataset Dimensions"):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(f"Number of Rows: **{df.shape[0]}**")

    with col3:
        st.write(f"Number of Columns: **{df.shape[1]}**")