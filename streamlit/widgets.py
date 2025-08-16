import streamlit as st
import pandas as pd
st.title("hellow loser")

name = st.text_input("enter your name")

age = st.slider("select your age:", 0,100,25)
st.write(f"your age is{age}")
option = ["python","java","c++","c","javascript"]
choice = st.selectbox("choose your favorit lanuage",option)
st.write(f"you selected {choice}")

if name:
    
    st.write(f"hellow to the most useless person in the world; dear{name}")
    
data = {
    "name" : ["masi" ,"mohi", "jake","john"],
    "age" : [29,28,30,15],
    "city" : ["new york", "boston","los angeles","tehran"]    
    
}
df = pd.DataFrame(data)
st.write(df)
df.to_csv("sampledata.csv")

uploaded_file = st.file_uploader("choose a csv",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)