import streamlit as st

def show_editor():
    st.subheader("🛠️ Paste your code below")
    return st.text_area("Game code:", height=300, key="code_input")
