import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="SuperStore!!",page_icon=":barchart:",layout="wide")

st.title(" :bar_chart: Sample SuperStore EDA")
st.markdown('<style>div.block-container{padding-top:lrem;}</style>',unsafe_allow_html=True)

f1=st.file_uploader(":file_folder:upload a file",type=(["csv","txt","xlsx","xls"]))
if f1 is not none:
    filename = f1.name
    st.write(filename)
    df=pd.read_csv(filename)
else:
    os.chdir(r"C:\Users\harsh\OneDrive\Desktop\Streamlit")
    df=pd.read_csv("Superstore.csv")


