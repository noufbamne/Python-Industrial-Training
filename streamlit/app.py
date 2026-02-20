import streamlit as st

#title
st.title("Machine Learning Project")

# header / subheader
st.header("This is a header.") #h1 tag

st.subheader("This is a Subheader.")

#text 
st.text("This is some text.")

# markdown
st.markdown("This is our first markdown")
st.markdown("#### This is our first markdown")

# error / colourful text
st.success("This is a success")
st.error("This is an error")

#information
st.info("This is information")

# warning
st.warning("This is a warning")

#exception
st.exception("This is an exception")

#help
import pandas
st.help(pandas)

#range function help
st.help(range)

#writing text suprer function
st.write("Hello Streamlit")
st.write(range(10))

#image
from PIL import Image

img = Image.open("Python/streamlit/imgdark.jpg")
st.image(img)
