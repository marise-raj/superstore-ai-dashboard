import streamlit as st
import pandas as pd
from groq import Groq

# ---- SETUP ----
st.title("🛒 Superstore AI Sales Assistant")
st.write("Ask any question about the sales data in plain English.")

# Load your data
df = pd.read_csv("superstore_clean.csv")

# Connect to Groq (paste your API key below)
client = Groq(api_key="Paste Your API KEY")

# ---- USER INPUT ----
question = st.text_input("Ask a question about the sales data:")

if question:
    # Give the AI a summary of the data to understand it
    data_summary = df.describe(include="all").to_string()
    columns_info = ", ".join(df.columns)

    prompt = f"""
    You are a data analyst. Here is a summary of a sales dataset.
    Columns: {columns_info}
    Summary statistics: {data_summary}

    Answer this question based on the data: {question}
    Give a clear, short, business-friendly answer.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    st.write("### Answer:")
    st.write(response.choices[0].message.content)