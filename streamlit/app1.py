import streamlit as st

#title
st.title("Machine Learning Project")

#image
from PIL import Image
img = Image.open("Python/streamlit/imgdark.jpg")
st.image(img, width = 300, caption = "Aesthetic image")