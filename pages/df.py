import streamlit as st
import pandas as pd

st.write(pd.DataFrame({
    'Название': [],
    'Цена': [],
    'Статус' : [],
    'Кратность' : [] #Add data with floUer
}))