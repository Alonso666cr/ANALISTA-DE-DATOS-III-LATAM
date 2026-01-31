"""
APLICACIÓN STREAMLIT - ANÁLISIS ESTADÍSTICO EXPLORATORIO
=========================================================
Análisis estadístico descriptivo interactivo
Autor: Apache (Andrés Cervantes)
Fecha: Enero 2026
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import io

# Configuración de la página
st.set_page_config(
    page_title="Análisis Estadístico Exploratorio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo de gráficas
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# =====================================================================
# TÍTULO Y DESCRIPCIÓN
# =====================================================================
st.title("📊 Análisis Estadístico Descriptivo - Demostración")
st.markdown("""
### Herramienta Interactiva de Análisis Exploratorio de Datos (EDA)

Esta aplicación ejemplifica el uso e interpretación de:
- **Medidas de posición**: promedio, mediana, moda, cuantiles
- **Medidas de variabilidad**: rango, varianza, desviación estándar, CV
- **Medidas de asociación**: Correlación de Pearson, Rho de Spearman, Chi-cuadrado

**Dataset**: Datos de estudiantes con calificaciones y características demográficas
""")

st.divider()

# =====================================================================
# CARGA DE DATOS
# =====================================================================
@st.cache_data
def cargar_datos():
    """Carga los datos desde CSV"""
    try:
        df = pd.read_csv('estudiantes_datos.csv')
        return df
    except:
        # Crear datos de ejemplo si no existe el archivo
        np.random.seed(42)
        n = 50
        data = {
            'Estudiante': [f'Estudiante_{i+1}' for i in range(n)],
            'Edad': np.random.choice([18, 19, 20], n),
            'Calificacion_Matematicas': np.random.randint(54, 96, n),
            'Calificacion_Ciencias': np.random.randint(56, 96, n),
            'Horas_Estudio': np.random.randint(1, 9, n),
            'Nivel_Socioeconomico': np.random.choice(['Alto', 'Medio', 'Bajo'], n),
            'Aprobado': np.random.choice(['Si', 'No'], n, p=[0.9, 0.1])
        }
        return pd.DataFrame(data)

df = cargar_datos()

# =====================================================================
# SIDEBAR - OPCIONES
# =====================================================================
st.sidebar.header("⚙️ Configuración")
st.sidebar.markdown("---")

# Selector de secciones
seccion = st.sidebar.radio(
    "Seleccione la sección de análisis:",
    [
        "📋 Exploración Inicial",
        "📍 Medidas de Posición",
        "📏 Medidas de Variabilidad",
        "🔗 Medidas de Asociación",
        "📊 Visualizaciones",
        "📑 Resumen Completo"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(f"**Registros**: {len(df)}\n\n**Variables**: {len(df.columns)}")

# =====================================================================
# SECCIÓN: EXPLORACIÓN INICIAL
# =====================================================================
if seccion == "📋 Exploración Inicial":
    st.header("📋 Exploración Inicial de los Datos")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de Registros", len(df))
    with col2:
        st.metric("Total de Variables", len(df.columns))
    with col3:
        st.metric("Valores Faltantes", df.isnull().sum().sum())
    
    st.subheader("Vista previa de los datos")
    st.dataframe(df.head(10), use_container_width=True)
    
    st.subheader("Tipos de datos por