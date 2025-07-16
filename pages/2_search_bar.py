import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import plotly.express as px


# 숫자로 되어 있는 파일을 넣어주면 사이드 메뉴를 순서에 맞게 넣어줌


ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']



# 텍스트를 입력 받고 해당 이미지를 보여주자
ani_name = st.text_input('Enter the name of animation')


if ani_name:
    for ani in ani_list:
        if ani_name in ani:
            st.image(img_list[ani_list.index(ani)])

        
# 변화가 많은 
df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)



# Plotly Bar Chart
fig = px.bar(
    df,
    x="command",     # x축에 command
    y="rating",      # y축에 rating
    color="command", # command별 색깔 구분
    labels={"command": "x축 제목", "rating": "Rating"},
    title="Command Rating Bar Chart"
)

st.plotly_chart(fig)


