import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit Hello World') # タイトル

st.write('DataFrame') # テキストの表示

df = pd.DataFrame({ 'lat': [35.705], 'lon': [139.7150] }) 
st.write("df shape:", df.shape) 
st.write(df.head()) 
df['lat'] = df['lat'].astype(float) 
df['lon'] = df['lon'].astype(float) 
df.dtypes 
print(df.columns) 
st.write(df) 
st.write("ゆりかの家")
st.map(df) # 地図の表示