import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')


target = st.number_input('How much do you want to save?', value=int)
deposit = st.number_input('How much have you saved already?')
contr = st.number_input('How much can you save a month?')
t = st.number_input('in how many years do you want to achieve your goal?')

r = 0.05
n = 12


saved = deposit * (1 + r / n) ** (n * t) + contr * (((1 + r / n) ** (n * t) - 1) / (r / n));

progress = saved / target * 100

st.write('Your progress is', progress)
