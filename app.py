# app.py - Streamlit frontend for Simple Agent
import streamlit as st
from agent import SimpleAgent

# Title
st.set_page_config(page_title="AI Agent Demo", layout="wide")
st.title("🤖 Simple AI Agent with A2A + Streamlit")

# Initialize agent
agent = SimpleAgent()

# User Input
user_input = st.text_input("Enter your query:", "")

# Run Agent
if st.button("Run Agent"):
    if user_input.strip():
        with st.spinner("Running agent..."):
            output = agent.run_agent(user_input)
        st.success(output)
    else:
        st.warning("Please enter some text first.")
