import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')


target = st.number_input('How much do you want to save?')
deposit = st.number_input('How much have you saved already?')
contr = st.number_input('How much can you save a month?')
t = st.number_input('in how many years do you want to achieve your goal?')

r = 0.05
n = 12


saved = deposit * (1 + r / n) ** (n * t) + contr * (((1 + r / n) ** (n * t) - 1) / (r / n));

if target == 0: st.write('Your progress is', '0%')
else: st.write('Your progress is', saved / target * 100) 



chart_data = pd.DataFrame(
     np.random.randn(20, 1),
     columns=['a'])

st.line_chart(chart_data)
