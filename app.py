import streamlit as st
from PIL import Image

st.title("호박벌 사진")

# 이미지 불러오기 (bee.jpg는 같은 폴더에 있어야 함)
image = Image.open("bee.jpg")

st.image(image, caption="호박벌", use_column_width=True)
