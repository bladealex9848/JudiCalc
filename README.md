# JudiCalc: Calculadora de Días Hábiles para la Rama Judicial de Colombia

## Tabla de Contenidos
1. [Descripción](#descripción)
2. [Características](#características)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Instalación](#instalación)
5. [Uso](#uso)
6. [Manual Técnico](#manual-técnico)
7. [Manual de Usuario](#manual-de-usuario)
8. [Contribución](#contribución)
9. [Registro de Cambios](#registro-de-cambios)
10. [Créditos](#créditos)
11. [Licencia](#licencia)

## Descripción

JudiCalc es una herramienta web interactiva diseñada específicamente para funcionarios y administrativos de la Rama Judicial de Colombia. Esta aplicación permite calcular con precisión los días hábiles entre dos fechas dadas, teniendo en cuenta los fines de semana, días festivos nacionales y las particularidades de diferentes especialidades judiciales.

## Características Principales

- **Cálculo Preciso de Días Hábiles**: Considera fines de semana y festivos nacionales.
- **Adaptación a Especialidades Judiciales**: Incluye cálculos para Colectiva, Individual Penal, Ejecución de penas y promiscuos de familia.
- **Visualización de Días Hábiles por Mes**: Muestra una tabla detallada por especialidad.
- **Interfaz de Usuario Intuitiva**: Desarrollada con Streamlit para una experiencia web fluida.
- **Capacidad de Adaptación Anual**: Actualmente configurado para 2023, con posibilidad de expansión.

## Estructura del Proyecto
```
JudiCalc/
│
├── app.py
├── test_judicialc.py
├── holidays_2023.json
├── dias_habiles_2023.csv
│
├── assets/
│   └── logo.png
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Instalación

1. Clonar el repositorio:
   ```
   git clone https://github.com/tu-usuario/JudiCalc.git
   ```
2. Navegar al directorio del proyecto:
   ```
   cd JudiCalc
   ```
3. Crear un entorno virtual:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows use `venv\Scripts\activate`
   ```
4. Instalar las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Uso

Para ejecutar la aplicación:
```
streamlit run app.py
```
Siga las instrucciones en la interfaz de usuario para seleccionar fechas y calcular días hábiles.

## Manual Técnico

[Aquí puedes incluir detalles técnicos sobre la implementación, estructura del código, etc.]

## Manual de Usuario

[Aquí puedes incluir instrucciones detalladas sobre cómo usar la aplicación]

## Contribución

Las contribuciones son bienvenidas. Por favor, abra un issue para discutir cambios mayores antes de hacer un pull request.

## Registro de Cambios

- 2023-08-12: Versión inicial (v1.0.0)
  - Implementación del cálculo de días hábiles para el año 2023
  - Interfaz web con Streamlit

## Créditos

Desarrollado y mantenido por Alexander Oviedo Fadul, Profesional Universitario Grado 11 en el Consejo Seccional de la Judicatura de Sucre.

[GitHub](https://github.com/bladealex9848) | [Website](https://alexander.oviedo.isabellaea.com/) | [Instagram](https://www.instagram.com/alexander.oviedo.fadul) | [Twitter](https://twitter.com/alexanderofadul) | [Facebook](https://www.facebook.com/alexanderof/) | [WhatsApp](https://api.whatsapp.com/send?phone=573015930519&text=Hola%20!Quiero%20conversar%20contigo!) | [LinkedIn](https://www.linkedin.com/in/alexander-oviedo-fadul-49434b9a/)

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - vea el archivo [MIT License](https://opensource.org/licenses/MIT) para más detalles.