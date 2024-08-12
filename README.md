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
│
├── assets/
│   └── logo.png
│   └── holidays_2023.json
│   └── dias_habiles_2023.csv
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

### Componentes Principales

#### 1. Función `load_data(year)`
- Carga los días festivos desde un archivo JSON.
- Lee el CSV de días hábiles y lo convierte en un diccionario.
- Maneja errores si los archivos no se encuentran.

#### 2. Función `calculate_working_days(start_date, end_date, specialty, working_days)`
- Calcula los días hábiles entre dos fechas para una especialidad específica.
- Utiliza los datos del CSV para determinar los días hábiles por mes.
- Ajusta el cálculo para meses parciales al inicio y final del período.

#### 3. Interfaz de Usuario (Streamlit)
- Configura la página y el sidebar.
- Maneja la selección de fechas y especialidad.
- Muestra resultados y tabla de días hábiles.

### Flujo de Datos

1. El usuario selecciona el año, las fechas y la especialidad.
2. Se cargan los datos de días festivos y hábiles.
3. Se calcula el número de días hábiles.
4. Se muestra el resultado y la tabla de días hábiles por mes.

### Manejo de Errores

- Validación de fechas de entrada.
- Manejo de archivos no encontrados con mensajes de advertencia.
- Uso de datos por defecto si no se encuentran los archivos necesarios.

### Consideraciones de Rendimiento

- La aplicación está optimizada para cálculos rápidos utilizando operaciones vectorizadas de Pandas.
- Los datos se cargan una sola vez al inicio, mejorando el tiempo de respuesta para cálculos subsiguientes.

### Seguridad

- No se almacenan datos sensibles del usuario.
- Los archivos de datos están en formato JSON y CSV, que son fáciles de auditar.

### Mantenimiento y Actualización

Para añadir soporte para un nuevo año:
1. Crear `holidays_[AÑO].json` en la carpeta `assets`.
2. Crear `dias_habiles_[AÑO].csv` en la carpeta `assets`.
3. Actualizar la lista de años disponibles en el selectbox del sidebar.

## Manual de Usuario

### Introducción

JudiCalc es una herramienta diseñada para calcular días hábiles en el contexto judicial colombiano. Permite a los usuarios determinar el número de días hábiles entre dos fechas, considerando diferentes especialidades judiciales.

### Acceso a la Aplicación

1. Abra su navegador web.
2. Visite la URL: [https://judicalc.streamlit.app](https://judicalc.streamlit.app)

### Uso de la Aplicación

#### 1. Selección del Año
- En el sidebar, elija el año para el cual desea realizar el cálculo.

#### 2. Elección de la Especialidad
- También en el sidebar, seleccione la especialidad judicial relevante:
  - Colectiva
  - Individual Penal
  - Individual Ejecución de penas y promiscuos de familia

#### 3. Selección de Fechas
- En el área principal, use los selectores de fecha para elegir:
  - Fecha de inicio
  - Fecha de fin

#### 4. Cálculo de Días Hábiles
- Una vez seleccionadas las fechas, la aplicación automáticamente calculará y mostrará el número de días hábiles.

#### 5. Visualización de Resultados
- El resultado se muestra en un mensaje de éxito, indicando el número de días hábiles entre las fechas seleccionadas.
- Debajo del resultado, se muestra una tabla con el desglose de días hábiles por mes para el año seleccionado.

### Funcionalidades Adicionales

#### Carga de Archivo de Días Festivos Personalizado
- En el sidebar, puede cargar un archivo JSON con días festivos personalizados.
- Útil para casos especiales o para probar diferentes escenarios.

#### Recursos Adicionales
- En el sidebar, expanda la sección "Recursos Adicionales" para acceder a:
  - Manual de Usuario
  - Formulario para Reportar Problemas

### Interpretación de Resultados

- El número de días hábiles mostrado excluye fines de semana y días festivos.
- La tabla de días hábiles por mes muestra el desglose para cada especialidad, útil para comparaciones y verificaciones.

### Solución de Problemas Comunes

1. **Las fechas no se pueden seleccionar**: Asegúrese de que la fecha de inicio sea anterior a la fecha de fin.
2. **El cálculo parece incorrecto**: Verifique la especialidad seleccionada y el año, ya que los días hábiles pueden variar.
3. **Error al cargar archivo personalizado**: Asegúrese de que el archivo esté en formato JSON válido.

### Contacto y Soporte

Para obtener ayuda adicional o reportar problemas:
- Visite nuestra [página de GitHub](https://github.com/bladealex9848/JudiCalc/issues)
- Contacte al desarrollador a través de los enlaces proporcionados en el sidebar de la aplicación.

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