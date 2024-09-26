import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Streamlit App")
st.write("Here's our first attempt at using data to create a table:")

st.write(pd.DataFrame({
  'first column':[1,2,3,4],
  'second column': [10,20,30,40]
}))

if st.button('Say Hello'):
  st.write('Why Hello there!')
else:
  st.write('Goodbye')
chart_data = pd.DataFrame(
  np.reandom.randn(20, 3),
  columns=['a','b','c'])

st.line_chart(chart_data)
  
