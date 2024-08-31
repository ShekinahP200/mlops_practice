import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Cache the data loading function
@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

# Load the data
df, target_names = load_data()

# Train the model
model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])

# Initialize StandardScaler
scaler = StandardScaler()
scaler.fit(df.iloc[:, :-1])

# Sidebar for user input
st.sidebar.title("Input Features")
sepal_length = st.sidebar.slider("Sepal length (cm)", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
sepal_width = st.sidebar.slider("Sepal width (cm)", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
petal_length = st.sidebar.slider("Petal length (cm)", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
petal_width = st.sidebar.slider("Petal width (cm)", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))

# Prepare input data for prediction
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
input_data_scaled = scaler.transform(input_data)  # Scale the input data

# Prediction
prediction = model.predict(input_data_scaled)
predicted_species = target_names[prediction[0]]

# Display the result
st.write("Prediction")
st.write(f"The predicted species is: {predicted_species}")
