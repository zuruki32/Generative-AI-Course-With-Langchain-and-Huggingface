import streamlit as st
import pandas as pd
import numpy as np


#title of the app
st.title("hellow loser")
st.write("here is the day of your result")

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column':[10,20,30,40]
    
})

st.write("here is the datafame") 
st.write(df)

chart_data = pd.DataFrame(
    
   np.random.randn(20,3), columns=['a','b','c']
        
)
st.line_chart(chart_data)