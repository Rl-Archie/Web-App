import streamlit as st
from PIL import Image

st.subheader("Color to GrayScale Image Convertor")

upd = st.file_uploader("Browse Files")

with st.expander("Start Camera"):
    # Start Cam.
    picture = st.camera_input("Camera")

if picture:
    #Create pillow img instance.
    img = Image.open(picture)

    #Convert pillow img to grayscale.
    gray_img = img.convert("L")

    #Display GrayScale image.
    st.image(gray_img)

if upd:
    upd = Image.open(upd)

    gray_upd = upd.convert("L")

    st.image(gray_upd)



