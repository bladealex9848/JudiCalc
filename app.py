import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import json

def load_holidays(year):
    with open(f'assets/holidays_{year}.json', 'r') as f:
        return json.load(f)

def calculate_working_days(start_date, end_date, specialty, holidays):
    working_days = 0
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() < 5 and current_date.strftime('%Y-%m-%d') not in holidays:
            working_days += 1
        current_date += timedelta(days=1)
    
    if specialty == 'Colectiva' and current_date.month == 12:
        working_days -= 7
    
    return working_days

st.set_page_config(
    page_title="JudiCalc - Calculadora de Días Hábiles",
    page_icon="📅",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://alexander.oviedo.isabellaea.com/',
        'Report a bug': 'https://github.com/bladealex9848/JudiCalc/issues',        
        'About': "JudiCalc: Calculadora de Días Hábiles para la Rama Judicial de Colombia"
    }
)

st.sidebar.image("assets/logo.png", width=200)
st.sidebar.title("Recursos Adicionales")
with st.sidebar.expander("Ver Recursos Adicionales", expanded=False):
    st.markdown("[Manual de Usuario](https://github.com/bladealex9848/JudiCalc/wiki)")
    st.markdown("[Reportar un Problema](https://github.com/bladealex9848/JudiCalc/issues)")

st.title("JudiCalc: Calculadora de Días Hábiles Judiciales")

st.write("""
[![ver código fuente](https://img.shields.io/badge/Ver%20en-GitHub-blue?logo=github)](https://github.com/bladealex9848/JudiCalc)
![Visitantes](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fjudicalc.streamlit.app&label=Visitantes&labelColor=%235d5d5d&countColor=%231e7ebf&style=flat)
""")

year = st.sidebar.selectbox("Seleccione el año", [2023])
holidays = load_holidays(year)

specialty = st.sidebar.selectbox(
    "Seleccione la especialidad",
    ["Colectiva", "Individual Penal", "Individual Ejecucion de penas y promiscuos de familia"]
)

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Fecha de inicio", datetime(year, 1, 1))
with col2:
    end_date = st.date_input("Fecha de fin", datetime(year, 12, 31))

if start_date > end_date:
    st.error("La fecha de inicio debe ser anterior a la fecha de fin.")
else:
    working_days = calculate_working_days(start_date, end_date, specialty, holidays)
    
    st.success(f"Días hábiles entre {start_date} y {end_date} para la especialidad {specialty}: {working_days}")

    # Leer desde el año seleccionado y mostrar en una tabla, sino mostrar mensaje de error
    try:
        st.subheader(f'Días hábiles por mes en {year}')
        df = pd.read_csv(f'assets/dias_habiles_{year}.csv')
        st.table(df)
    except FileNotFoundError:
        st.error("No se encontró el archivo de festivos para el año seleccionado.")    
    
st.sidebar.markdown("---")
st.sidebar.write("Desarrollado por Alexander Oviedo Fadul")
st.sidebar.write("Consejo Seccional de la Judicatura de Sucre")
st.sidebar.write("v.1.0.0")
st.sidebar.write("[GitHub](https://github.com/bladealex9848) | [Website](https://alexander.oviedo.isabellaea.com/) | [LinkedIn](https://www.linkedin.com/in/alexander-oviedo-fadul-49434b9a/)")