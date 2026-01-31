"""
ANÁLISIS ESTADÍSTICO DESCRIPTIVO - STREAMLIT VERSION
=========================================================
Conversión directa del notebook manteniendo la misma lógica
Este código usa las MISMAS librerías y MISMA lógica que el notebook original
Solo se adaptan los outputs para Streamlit
Autor: Apache
Fecha: Enero 2026
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import io

# =============================================================================
# CONFIGURACIÓN DE STREAMLIT
# =============================================================================
st.set_page_config(
    page_title="Análisis Estadístico Descriptivo",
    page_icon="📊",
    layout="wide"
)

# Configurar estilo de gráficas (igual que el notebook)
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# =============================================================================
# TÍTULO PRINCIPAL
# =============================================================================
st.title("ANÁLISIS ESTADÍSTICO DESCRIPTIVO - PROYECTO DEMOSTRACIÓN")
st.markdown("""
Este código ejemplifica el uso e interpretación de:
- Medidas de posición (promedio, mediana, moda, cuantiles)
- Medidas de variabilidad (rango, mínimo, máximo, varianza, desviación estándar, CV)
- Medidas de asociación (Correlación de Pearson, Chi-cuadrado, Rho de Spearman)

**Dataset:** Datos de estudiantes con calificaciones y características demográficas
""")

st.divider()

# =============================================================================
# 1. IMPORTACIÓN DE LIBRERÍAS NECESARIAS
# =============================================================================
st.header("PASO 1: Importando librerías necesarias...")
st.success("✓ Librerías importadas correctamente")

# =============================================================================
# 2. CARGA DE DATOS DESDE ARCHIVO CSV
# =============================================================================
st.header("PASO 2: Cargando datos desde archivo CSV...")

@st.cache_data
def cargar_datos():
    try:
        df = pd.read_csv('estudiantes_datos.csv')
        return df
    except:
        st.error("❌ No se encontró el archivo 'estudiantes_datos.csv'")
        st.info("📝 Por favor, suba el archivo CSV en su repositorio de GitHub")
        st.stop()

df = cargar_datos()

st.success("✓ Datos cargados exitosamente")
st.write(f"✓ Número de registros: {len(df)}")
st.write(f"✓ Número de variables: {len(df.columns)}")

st.subheader("Primeros registros del dataset:")
st.dataframe(df.head(10))

# =============================================================================
# 3. EXPLORACIÓN INICIAL DE LOS DATOS
# =============================================================================
st.header("PASO 3: Exploración inicial de los datos")

st.subheader("Tipos de datos por columna:")
st.write(df.dtypes)

st.subheader("Información general del dataset:")
buffer = io.StringIO()
df.info(buf=buffer)
st.text(buffer.getvalue())

st.subheader("Verificación de valores nulos:")
st.write(df.isnull().sum())

# =============================================================================
# 4. MEDIDAS DE POSICIÓN (TENDENCIA CENTRAL)
# =============================================================================
st.header("PASO 4: MEDIDAS DE POSICIÓN (TENDENCIA CENTRAL)")

# Seleccionar variables numéricas para análisis (igual que en el notebook)
variables_numericas = ['Edad', 'Calificacion_Matematicas', 'Calificacion_Ciencias', 'Horas_Estudio']

for variable in variables_numericas:
    st.subheader(f"--- Análisis de: {variable} ---")
    
    # 4.1 PROMEDIO (Media aritmética)
    promedio = df[variable].mean()
    st.write(f"**Promedio (Media):** {promedio:.2f}")
    st.write(f"  *Interpretación:* El valor promedio de {variable} es {promedio:.2f}")
    
    # 4.2 MEDIANA (Percentil 50)
    mediana = df[variable].median()
    st.write(f"**Mediana:** {mediana:.2f}")
    st.write(f"  *Interpretación:* El 50% de los datos están por debajo de {mediana:.2f}")
    
    # 4.3 MODA (Valor más frecuente)
    moda = df[variable].mode()
    if len(moda) > 0:
        st.write(f"**Moda:** {moda.values[0]:.2f}")
        st.write(f"  *Interpretación:* El valor más frecuente es {moda.values[0]:.2f}")
    
    # 4.4 CUANTILES (Q1, Q2, Q3)
    q1 = df[variable].quantile(0.25)
    q2 = df[variable].quantile(0.50)
    q3 = df[variable].quantile(0.75)
    
    st.write(f"**Cuartil 1 (Q1 - 25%):** {q1:.2f}")
    st.write(f"  *Interpretación:* El 25% de los datos están por debajo de {q1:.2f}")
    st.write(f"**Cuartil 2 (Q2 - 50%):** {q2:.2f} (igual a la mediana)")
    st.write(f"**Cuartil 3 (Q3 - 75%):** {q3:.2f}")
    st.write(f"  *Interpretación:* El 75% de los datos están por debajo de {q3:.2f}")
    
    st.markdown("---")

# =============================================================================
# 5. MEDIDAS DE VARIABILIDAD (DISPERSIÓN)
# =============================================================================
st.header("PASO 5: MEDIDAS DE VARIABILIDAD (DISPERSIÓN)")

for variable in variables_numericas:
    st.subheader(f"--- Análisis de dispersión: {variable} ---")
    
    # 5.1 MÍNIMO Y MÁXIMO
    minimo = df[variable].min()
    maximo = df[variable].max()
    st.write(f"**Mínimo:** {minimo:.2f}")
    st.write(f"**Máximo:** {maximo:.2f}")
    
    # 5.2 RANGO
    rango = maximo - minimo
    st.write(f"**Rango:** {rango:.2f}")
    st.write(f"  *Interpretación:* La diferencia entre el valor máximo y mínimo es {rango:.2f}")
    
    # 5.3 VARIANZA
    varianza = df[variable].var()
    st.write(f"**Varianza:** {varianza:.2f}")
    st.write(f"  *Interpretación:* Medida de dispersión promedio al cuadrado")
    
    # 5.4 DESVIACIÓN ESTÁNDAR
    desviacion_std = df[variable].std()
    st.write(f"**Desviación Estándar:** {desviacion_std:.2f}")
    st.write(f"  *Interpretación:* En promedio, los datos se desvían {desviacion_std:.2f} unidades de la media")
    
    # 5.5 COEFICIENTE DE VARIACIÓN (CV)
    promedio = df[variable].mean()
    coef_variacion = (desviacion_std / promedio) * 100
    st.write(f"**Coeficiente de Variación (CV):** {coef_variacion:.2f}%")
    st.write(f"  *Interpretación:* La desviación estándar representa el {coef_variacion:.2f}% de la media")
    if coef_variacion < 15:
        st.write(f"  -> Baja variabilidad (datos homogéneos)")
    elif coef_variacion < 30:
        st.write(f"  -> Variabilidad moderada")
    else:
        st.write(f"  -> Alta variabilidad (datos heterogéneos)")
    
    st.markdown("---")

# =============================================================================
# 6. RESUMEN ESTADÍSTICO COMPLETO
# =============================================================================
st.header("PASO 6: RESUMEN ESTADÍSTICO COMPLETO")

st.subheader("Estadísticas descriptivas de todas las variables numéricas:")
resumen = df[variables_numericas].describe()
st.dataframe(resumen)

# =============================================================================
# 7. MEDIDAS DE ASOCIACIÓN - CORRELACIÓN DE PEARSON
# =============================================================================
st.header("PASO 7: MEDIDAS DE ASOCIACIÓN - CORRELACIÓN DE PEARSON")

st.write("""
La correlación de Pearson mide la relación lineal entre dos variables.
Rango: -1 (correlación negativa perfecta) a +1 (correlación positiva perfecta)
Cerca de 0: no hay correlación lineal
""")

# Calcular matriz de correlación de Pearson
matriz_correlacion = df[variables_numericas].corr(method='pearson')

st.subheader("Matriz de Correlación de Pearson:")
st.dataframe(matriz_correlacion)

# Ejemplo específico: correlación entre Matemáticas y Ciencias
correlacion_mat_cie, p_valor = stats.pearsonr(
    df['Calificacion_Matematicas'], 
    df['Calificacion_Ciencias']
)

st.subheader("--- Ejemplo detallado ---")
st.write("Correlación entre Calificación de Matemáticas y Ciencias:")
st.write(f"**Coeficiente de Pearson (r):** {correlacion_mat_cie:.4f}")
st.write(f"**P-valor:** {p_valor:.6f}")

if p_valor < 0.05:
    st.success(f"✓ La correlación ES estadísticamente significativa (p < 0.05)")
else:
    st.error(f"✗ La correlación NO es estadísticamente significativa (p >= 0.05)")

if abs(correlacion_mat_cie) < 0.3:
    st.write(f"*Interpretación:* Correlación débil")
elif abs(correlacion_mat_cie) < 0.7:
    st.write(f"*Interpretación:* Correlación moderada")
else:
    st.write(f"*Interpretación:* Correlación fuerte")

# =============================================================================
# 8. MEDIDAS DE ASOCIACIÓN - RHO DE SPEARMAN
# =============================================================================
st.header("PASO 8: MEDIDAS DE ASOCIACIÓN - RHO DE SPEARMAN")

st.write("""
Rho de Spearman mide la relación monotónica (no necesariamente lineal).
Se basa en rangos ordenados de los datos.
Útil cuando los datos no siguen una distribución normal.
""")

# Calcular matriz de correlación de Spearman
matriz_spearman = df[variables_numericas].corr(method='spearman')

st.subheader("Matriz de Correlación de Spearman:")
st.dataframe(matriz_spearman)

# Ejemplo específico
spearman_mat_horas, p_valor_sp = stats.spearmanr(
    df['Calificacion_Matematicas'], 
    df['Horas_Estudio']
)

st.subheader("--- Ejemplo detallado ---")
st.write("Correlación entre Calificación de Matemáticas y Horas de Estudio:")
st.write(f"**Coeficiente de Spearman (ρ):** {spearman_mat_horas:.4f}")
st.write(f"**P-valor:** {p_valor_sp:.6f}")

if p_valor_sp < 0.05:
    st.success(f"✓ La correlación ES estadísticamente significativa (p < 0.05)")
else:
    st.error(f"✗ La correlación NO es estadísticamente significativa (p >= 0.05)")

# =============================================================================
# 9. MEDIDAS DE ASOCIACIÓN - CHI-CUADRADO (χ²)
# =============================================================================
st.header("PASO 9: MEDIDAS DE ASOCIACIÓN - CHI-CUADRADO (χ²)")

st.write("""
Chi-cuadrado evalúa la independencia entre variables categóricas.
H0: Las variables son independientes
H1: Las variables están asociadas
""")

# Crear tabla de contingencia entre Nivel Socioeconómico y Aprobado
tabla_contingencia = pd.crosstab(
    df['Nivel_Socioeconomico'], 
    df['Aprobado']
)

st.subheader("Tabla de Contingencia (Nivel Socioeconómico vs Aprobado):")
st.dataframe(tabla_contingencia)

# Realizar prueba de Chi-cuadrado
chi2, p_valor_chi, grados_libertad, frecuencias_esperadas = stats.chi2_contingency(tabla_contingencia)

st.subheader("Resultados de la prueba Chi-cuadrado:")
st.write(f"**Estadístico Chi-cuadrado (χ²):** {chi2:.4f}")
st.write(f"**P-valor:** {p_valor_chi:.6f}")
st.write(f"**Grados de libertad:** {grados_libertad}")

st.subheader("Frecuencias esperadas (si fueran independientes):")
freq_esp_df = pd.DataFrame(
    frecuencias_esperadas, 
    index=tabla_contingencia.index, 
    columns=tabla_contingencia.columns
)
st.dataframe(freq_esp_df)

if p_valor_chi < 0.05:
    st.success(f"✓ Rechazamos H0: Las variables SÍ están asociadas (p < 0.05)")
    st.write(f"  Existe relación entre el Nivel Socioeconómico y Aprobar")
else:
    st.error(f"✗ No rechazamos H0: Las variables son independientes (p >= 0.05)")
    st.write(f"  No hay evidencia de relación entre Nivel Socioeconómico y Aprobar")

# =============================================================================
# 10. VISUALIZACIONES GRÁFICAS
# =============================================================================
st.header("PASO 10: Generando visualizaciones gráficas...")

# Crear figura con múltiples subgráficas (IGUAL QUE EN EL NOTEBOOK)
fig = plt.figure(figsize=(16, 12))

# 10.1 HISTOGRAMA - Distribución de Calificaciones de Matemáticas
ax1 = plt.subplot(3, 3, 1)
plt.hist(df['Calificacion_Matematicas'], bins=15, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(df['Calificacion_Matematicas'].mean(), color='red', linestyle='--', linewidth=2, label='Media')
plt.axvline(df['Calificacion_Matematicas'].median(), color='green', linestyle='--', linewidth=2, label='Mediana')
plt.xlabel('Calificación')
plt.ylabel('Frecuencia')
plt.title('Distribución de Calificaciones de Matemáticas')
plt.legend()
plt.grid(True, alpha=0.3)

# 10.2 BOX PLOT - Comparación de calificaciones
ax2 = plt.subplot(3, 3, 2)
datos_boxplot = [df['Calificacion_Matematicas'], df['Calificacion_Ciencias']]
plt.boxplot(datos_boxplot, labels=['Matemáticas', 'Ciencias'])
plt.ylabel('Calificación')
plt.title('Box Plot - Comparación de Calificaciones')
plt.grid(True, alpha=0.3)

# 10.3 SCATTER PLOT - Correlación Matemáticas vs Ciencias
ax3 = plt.subplot(3, 3, 3)
plt.scatter(df['Calificacion_Matematicas'], df['Calificacion_Ciencias'], 
            alpha=0.6, s=50, color='purple')
plt.xlabel('Calificación Matemáticas')
plt.ylabel('Calificación Ciencias')
plt.title(f'Correlación Matemáticas vs Ciencias\n(r = {correlacion_mat_cie:.3f})')
z = np.polyfit(df['Calificacion_Matematicas'], df['Calificacion_Ciencias'], 1)
p = np.poly1d(z)
plt.plot(df['Calificacion_Matematicas'].sort_values(), 
         p(df['Calificacion_Matematicas'].sort_values()), 
         "r--", alpha=0.8, linewidth=2)
plt.grid(True, alpha=0.3)

# 10.4 HISTOGRAMA - Distribución de Horas de Estudio
ax4 = plt.subplot(3, 3, 4)
plt.hist(df['Horas_Estudio'], bins=8, color='lightcoral', edgecolor='black', alpha=0.7)
plt.axvline(df['Horas_Estudio'].mean(), color='red', linestyle='--', linewidth=2, label='Media')
plt.xlabel('Horas de Estudio')
plt.ylabel('Frecuencia')
plt.title('Distribución de Horas de Estudio')
plt.legend()
plt.grid(True, alpha=0.3)

# 10.5 MAPA DE CALOR - Matriz de Correlación de Pearson
ax5 = plt.subplot(3, 3, 5)
sns.heatmap(matriz_correlacion, annot=True, cmap='coolwarm', center=0, 
            square=True, linewidths=1, cbar_kws={"shrink": 0.8}, fmt='.3f')
plt.title('Mapa de Calor - Correlación de Pearson')

# 10.6 SCATTER PLOT - Horas de Estudio vs Calificación
ax6 = plt.subplot(3, 3, 6)
plt.scatter(df['Horas_Estudio'], df['Calificacion_Matematicas'], 
            alpha=0.6, s=50, color='green')
plt.xlabel('Horas de Estudio')
plt.ylabel('Calificación Matemáticas')
plt.title(f'Horas de Estudio vs Calificación\n(ρ = {spearman_mat_horas:.3f})')
plt.grid(True, alpha=0.3)

# 10.7 GRÁFICO DE BARRAS - Aprobados por Nivel Socioeconómico
ax7 = plt.subplot(3, 3, 7)
conteo = pd.crosstab(df['Nivel_Socioeconomico'], df['Aprobado'])
conteo.plot(kind='bar', ax=ax7, color=['salmon', 'lightgreen'], alpha=0.7)
plt.xlabel('Nivel Socioeconómico')
plt.ylabel('Cantidad de Estudiantes')
plt.title('Distribución de Aprobados por Nivel Socioeconómico')
plt.xticks(rotation=0)
plt.legend(title='Aprobado')
plt.grid(True, alpha=0.3, axis='y')

# 10.8 VIOLIN PLOT - Distribución de calificaciones por aprobado
ax8 = plt.subplot(3, 3, 8)
datos_violin = [
    df[df['Aprobado']=='Si']['Calificacion_Matematicas'],
    df[df['Aprobado']=='No']['Calificacion_Matematicas']
]
parts = plt.violinplot(datos_violin, positions=[1, 2], showmeans=True, showmedians=True)
plt.xticks([1, 2], ['Aprobado: Sí', 'Aprobado: No'])
plt.ylabel('Calificación Matemáticas')
plt.title('Distribución de Calificaciones por Estado de Aprobación')
plt.grid(True, alpha=0.3)

# 10.9 MAPA DE CALOR - Matriz de Correlación de Spearman
ax9 = plt.subplot(3, 3, 9)
sns.heatmap(matriz_spearman, annot=True, cmap='viridis', center=0, 
            square=True, linewidths=1, cbar_kws={"shrink": 0.8}, fmt='.3f')
plt.title('Mapa de Calor - Correlación de Spearman')

# Ajustar el espaciado entre gráficas
plt.tight_layout()

# MOSTRAR EN STREAMLIT (en lugar de plt.show())
st.pyplot(fig)
plt.close()

st.success("✓ Gráficas generadas exitosamente")

# =============================================================================
# 11. TABLA RESUMEN DE TODAS LAS MEDIDAS CALCULADAS
# =============================================================================
st.header("PASO 11: TABLA RESUMEN FINAL")

# Crear un resumen personalizado (IGUAL QUE EN EL NOTEBOOK)
resumen_completo = pd.DataFrame()

for variable in variables_numericas:
    resumen_completo[variable] = {
        'Media': df[variable].mean(),
        'Mediana': df[variable].median(),
        'Moda': df[variable].mode().values[0] if len(df[variable].mode()) > 0 else np.nan,
        'Mínimo': df[variable].min(),
        'Máximo': df[variable].max(),
        'Rango': df[variable].max() - df[variable].min(),
        'Q1 (25%)': df[variable].quantile(0.25),
        'Q3 (75%)': df[variable].quantile(0.75),
        'Varianza': df[variable].var(),
        'Desv. Estándar': df[variable].std(),
        'Coef. Variación (%)': (df[variable].std() / df[variable].mean()) * 100
    }

resumen_completo = resumen_completo.T
st.subheader("RESUMEN ESTADÍSTICO COMPLETO:")
st.dataframe(resumen_completo.round(2))

# =============================================================================
# 12. CONCLUSIONES FINALES
# =============================================================================
st.header("CONCLUSIONES DEL ANÁLISIS")

st.info("""
Este análisis demostró el uso e interpretación de:

**1. MEDIDAS DE POSICIÓN:**
   - Media, mediana y moda para identificar el centro de los datos
   - Cuantiles (Q1, Q2, Q3) para entender la distribución

**2. MEDIDAS DE VARIABILIDAD:**
   - Rango, varianza y desviación estándar para medir dispersión
   - Coeficiente de variación para comparar variabilidad entre variables

**3. MEDIDAS DE ASOCIACIÓN:**
   - Correlación de Pearson para relaciones lineales entre variables continuas
   - Rho de Spearman para relaciones monotónicas (más robusto)
   - Chi-cuadrado para analizar independencia entre variables categóricas

Las visualizaciones complementan el análisis numérico y facilitan la
interpretación de los resultados.
""")

st.success("✓ ANÁLISIS COMPLETADO EXITOSAMENTE")

# Footer
st.markdown("---")
st.markdown("""
**Autor:** Apache (Andrés Cervantes)  
**Contexto:** Analista de Datos III - LATAM  
**Fecha:** Enero 2026
""")
