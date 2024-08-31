import streamlit as st
import pandas as pd

# Title of the app
st.title("Streamlit Text Input")

# Input for the user's name
name = st.text_input("Enter your name:")

# Slider for selecting age
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"Your age is {age}.")

# Dropdown for selecting favorite programming language
options = ["Python", "Java", "C", "JavaScript"]
choice = st.selectbox("Choose your favorite language:", options)
st.write(f"You've selected {choice}.")

# Greeting if the name is provided
if name:
    st.write(f"Hello, {name}!")

# Sample data
data = {
    'name': ['John', 'Jane', 'Jake', 'Jill'],
    'age': [28, 29, 35, 46],
    'city': ["New York", "Los Angeles", "Chicago", "Houston"]
}

# Convert sample data to a DataFrame and save it as a CSV
df = pd.DataFrame(data)
df.to_csv('sampledata1.csv', index=False)
st.write(df)

# File uploader for CSV files
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    # Read the uploaded CSV file
    uploaded_df = pd.read_csv(uploaded_file)
    st.write(uploaded_df)
