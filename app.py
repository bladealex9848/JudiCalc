import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import json
import os

def load_data(year):
    holidays = []
    working_days = {}
    try:
        with open(f'assets/holidays_{year}.json', 'r') as f:
            holidays = json.load(f)
        df = pd.read_csv(f'assets/dias_habiles_{year}.csv')
        working_days = df.set_index('Mes').to_dict()
    except FileNotFoundError:
        st.warning(f"No se encontraron archivos para el año {year}. Usando datos por defecto.")
        holidays = ["2023-01-01", "2023-05-01", "2023-12-25"]  # Días festivos por defecto
    return holidays, working_days

def calculate_working_days(start_date, end_date, specialty, working_days):
    total_days = 0
    current_date = start_date
    while current_date <= end_date:
        month = current_date.strftime('%B').lower()  # Obtiene el nombre del mes en minúsculas
        month_es = {
            'january': 'Enero', 'february': 'Febrero', 'march': 'Marzo', 'april': 'Abril',
            'may': 'Mayo', 'june': 'Junio', 'july': 'Julio', 'august': 'Agosto',
            'september': 'Septiembre', 'october': 'Octubre', 'november': 'Noviembre', 'december': 'Diciembre'
        }[month]
        if month_es in working_days[specialty]:
            if current_date.month == start_date.month:
                days_in_month = (min(end_date, current_date.replace(day=1) + timedelta(days=32)).replace(day=1) - timedelta(days=1)).day
                days_to_count = days_in_month - start_date.day + 1
                total_days += (working_days[specialty][month_es] * days_to_count) // days_in_month
            elif current_date.month == end_date.month:
                total_days += (working_days[specialty][month_es] * end_date.day) // end_date.day
            else:
                total_days += working_days[specialty][month_es]
        current_date = (current_date.replace(day=1) + timedelta(days=32)).replace(day=1)  # Avanza al siguiente mes
    return total_days

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

if os.path.exists("assets/logo.png"):
    st.sidebar.image("assets/logo.png", width=200)
else:
    st.sidebar.warning("Logo no encontrado")

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
holidays, working_days = load_data(year)

# Opción para cargar archivo de días festivos personalizado
uploaded_file = st.sidebar.file_uploader("Cargar archivo de días festivos personalizado", type="json")
if uploaded_file is not None:
    holidays = json.load(uploaded_file)
    st.sidebar.success("Archivo de días festivos cargado con éxito")

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
    working_days_count = calculate_working_days(start_date, end_date, specialty, working_days)
    
    st.success(f"Días hábiles entre {start_date} y {end_date} para la especialidad {specialty}: {working_days_count}")

    st.subheader(f'Días hábiles por mes en {year}')
    df = pd.DataFrame(working_days)
    st.table(df)

st.sidebar.markdown("---")
st.sidebar.write("Desarrollado por Alexander Oviedo Fadul")
st.sidebar.write("Consejo Seccional de la Judicatura de Sucre")
st.sidebar.write("v.1.0.0")
st.sidebar.write("[GitHub](https://github.com/bladealex9848) | [Website](https://www.alexanderoviedofadul.dev/) | [LinkedIn](https://www.linkedin.com/in/alexander-oviedo-fadul/)")
