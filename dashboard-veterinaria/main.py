import pandas as pd
import plotly.express as px
import streamlit as st

file_path = 'Banco.csv'
df = pd.read_csv(file_path, thousands=',')

st.title('Dashboard de Diagnóstico Médico')

fig_hemoglobina = px.bar(df, x='Diagnóstico', y='Hemoglobina (g/dL)', title='Hemoglobina por Diagnóstico')
st.plotly_chart(fig_hemoglobina)

fig_linfocito = px.bar(df, x='Diagnóstico', y='Linfócitos (/µL)', title='Linfócitos por Diagnóstico')
st.plotly_chart(fig_linfocito)

st.subheader('Dados Originais')
st.write(df)
