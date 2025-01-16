from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate  # Correct import path
from langchain_core.output_parsers import StrOutputParser # Correct import path

import streamlit as st
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Set environment variables
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Define the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("user", "{user_input}")
])

# Streamlit app title
st.title("Langchain Google Generative AI")

# Input from the user
user_input = st.text_input("Enter your query:")

# Define the model and output parser
model = ChatGoogleGenerativeAI(model="gemini-pro")
output_parser = StrOutputParser()

# Combine prompt, model, and output parser into a chain
chain = prompt | model | output_parser

# Display the result if there is user input
if user_input:
    response = chain.invoke({"user_input": user_input})  # Correctly pass input to the chain
    st.write(response)
