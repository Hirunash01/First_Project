import streamlit as st

options = ('Hello', 'World')
st.sidebar.selectbox('Options', options  )
st.title('Hello')
st.write('This is my very First web app')