import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from agents.recommendation_agent import RecommendationAgent

import subprocess
import json

st.title("🎯 HyperRecs Recommendations")

user_id = st.text_input("Enter User ID", "user_1")

if st.button("Get Recommendations"):
    agent = RecommendationAgent()
    recs = agent.get_recommendations(user_id)
    if recs:
        st.write("## Recommended Products:")
        for r in recs:
            st.success(r)
    else:
        st.warning("No recommendations found for this user.")

# Ollama powered Q&A interface
st.write("---")
st.subheader("💬 Ask HyperRecs")
query = st.text_input("Ask a question about your preferences or products")

if st.button("Ask Ollama"):
    if query.strip():
        try:
            # Invoke local Ollama model
            result = subprocess.run(
                ["ollama", "run", "llama3", query],
                capture_output=True,
                text=True,
                check=True
            )
            st.text_area("Ollama says:", result.stdout, height=200)
        except subprocess.CalledProcessError as e:
            st.error("Ollama failed to respond.")
            st.code(e.stderr)
    else:
        st.info("Please enter a question to ask.")