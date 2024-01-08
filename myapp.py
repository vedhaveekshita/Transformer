import streamlit as st
st.set_page_config(page_title="Houses")
st.header("Types of houses")
col1,col2 = st.columns(2)
with col1:
  st.subheader("type1")
  st.image("./type 1.png",caption="type 1", width=300,use_column_width=True)
  st.write("big house")
with col2:
  st.subheader("type2")
  st.image("./type 2.png",caption="type 2", width=300,use_column_width=True)
  st.write("villa")
  
  
