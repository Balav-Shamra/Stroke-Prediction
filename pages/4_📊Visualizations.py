import streamlit as st
import pandas as pd
from PIL import Image
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Data Visualizations",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="expanded"
)

col1, col2 = st.columns(2)
with col1:
    st.write("*****")

    st.markdown('<h1 style="color:grey;font-weight:bold;text-algin:center;">Data Visualization</h1>',
                unsafe_allow_html=True)

    st.write("******")

with col2:
    img = Image.open("visualizations.jpeg")
    st.image(img, width=400, caption="Visualize Data")

st.subheader("Stroke Dataset")
df = pd.read_csv("CleanedStrokeData.csv")
st.dataframe(df.head())

with st.expander("Display Each Column"):
    cols = st.multiselect("Select Column", options=df.columns)
    if len(cols) == 0:
        st.write("No Data to Display")
    else:
        st.dataframe(df[cols].head(10))

fig1 = sns.histplot(data=df, x="stroke", hue="gender")
fig1.set_title("Stroke by Gender")
fig1.set_xlim(0, 1)
st.pyplot(plt.gcf())


fig2, (ax1, ax2) = plt.subplots(1,2)
ax1.set_title("Heart Disease Counts")
ax1.pie(df[["heart_disease"]].value_counts(), explode=[0,0.09,0], labels=["No", "Yes", ""])

ax2.set_title("Hypertension Counts")
ax2.pie(df[["hypertension"]].value_counts(), explode=[0,0.09,0], labels=["No", "Yes", ""])
st.pyplot(plt.gcf())
