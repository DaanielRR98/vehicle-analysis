import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Analisis de vehiculos en venta en EE.UU.')

car_data = pd.read_csv('vehicles_us.csv')

if st.button('Mostrar histograma del odometro'):
    st.write('Histograma: kilometraje (odometer)')
    fig_hist = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

if st.button('Mostrar grafico de dispersion'):
    st.write('Dispersion: odometro vs presio')
    fig2_hist = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig2_hist, use_container_width=True)