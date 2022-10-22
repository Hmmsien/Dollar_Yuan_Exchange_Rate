from tkinter.ttk import Style
import streamlit as st
import pandas as pd
import plotly.express as px

header = st.container()
dataset = st.container()
features = st.container()

st.markdown(
    """"
    <style>
    .main {
        background-color: #F5F5F5;
        color: #e08882;
    }
    </style>
    """,
    unsafe_allow_html=True
)
with header:
    st.title('Dollar Yuan Exchange Rate - 35 Year Historical Chart')
    st.text('In this project I look into the Dollar Yuan Exchange Rate in 35 years')  

with dataset:
    st.header('Dollar Yuan Exchange Rate dataset') 

    # Loading data
    df = pd.read_csv('./data/us-dollar-yuan-exchange-rate-historical-chart.csv', error_bad_lines=False)
    st.write(df.head(6))

    # Split data into per year, get mean value for each year
    st.subheader('Mean exchange rate in 35 years')
    df['year'] = pd.DatetimeIndex(df['date']).year
    df_year = df.groupby('year').mean()
    year_rate = pd.DataFrame(df_year)

    # Display plotly line chart
    fig = px.line(year_rate)
    st.write(fig)

with features:
    st.header('The features I created')
    

