import streamlit as st
import pandas as pd
import seaborn as sns
import datetime

number = st.number_input("Insert a number", value=100, placeholder="how much money you want")
st.write(number*100)
datetime.time()
start = datetime.date(2023,5,1)
end = datetime.date(2024,5,31)

d = st.date_input("select a date in May", max_value=end, min_value=start, format="MM/DD/YYYY")

t = st.time_input("Set an alarm for", datetime.time(12, 45),step=120)
st.write("Alarm is set for", t)


#picture = st.camera_input("Take a picture")

#if picture:
    #st.image(picture)

import cv2
import numpy as np

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # Check the type of cv2_img:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(cv2_img))

    # Check the shape of cv2_img:
    # Should output shape: (height, width, channels)
    st.write(cv2_img.shape)

uploaded_file = st.file_uploader("Choose a CSV file", accept_multiple_files=False,type='csv')
#.write(type(uploaded_file))
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    st.write(df.describe())
