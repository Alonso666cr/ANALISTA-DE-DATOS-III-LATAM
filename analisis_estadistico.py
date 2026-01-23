#!/usr/bin/env python
# coding: utf-8

# ANALISTA DE DATOS III - LATAM
# Costa Rica|req23818

# In[1]:


"""
ANÁLISIS ESTADÍSTICO DESCRIPTIVO - PROYECTO DEMOSTRACIÓN
=========================================================

Este código ejemplifica el uso e interpretación de:
- Medidas de posición (promedio, mediana, moda, cuantiles)
- Medidas de variabilidad (rango, mínimo, máximo, varianza, desviación estándar, CV)
- Medidas de asociación (Correlación de Pearson, Chi-cuadrado, Rho de Spearman)

Dataset: Datos de estudiantes con calificaciones y características demográficas
Autor: Apache
Fecha: Andrés Cervantes 2026
"""

# =============================================================================
# 1. IMPORTACIÓN DE LIBRERÍAS NECESARIAS
# =============================================================================
print("="*80)
print("PASO 1: Importando librerías necesarias...")
print("="*80)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Configurar estilo de gráficas para mejor visualización
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("✓ Librerías importadas correctamente\n")


# In[2]:


# =============================================================================
# 2. CARGA DE DATOS DESDE ARCHIVO CSV
# =============================================================================
print("="*80)
print("PASO 2: Cargando datos desde archivo CSV...")
print("="*80)

# Cargar el dataset desde archivo CSV
# Nota: Cambia la ruta si el archivo está en otra ubicación
ruta_archivo = 'estudiantes_datos.csv'
df = pd.read_csv(ruta_archivo)

print(f"✓ Datos cargados exitosamente")
print(f"✓ Número de registros: {len(df)}")
print(f"✓ Número de variables: {len(df.columns)}")
print(f"\nPrimeros registros del dataset:")
print(df.head(10))
print("\n")

# =============================================================================
# 3. EXPLORACIÓN INICIAL DE LOS DATOS
# =============================================================================
print("="*80)
print("PASO 3: Exploración inicial de los datos")
print("="*80)

print("\nTipos de datos por columna:")
print(df.dtypes)

print("\nInformación general del dataset:")
print(df.info())

print("\nVerificación de valores nulos:")
print(df.isnull().sum())
print("\n")

# =============================================================================
# 4. MEDIDAS DE POSICIÓN (TENDENCIA CENTRAL)
# =============================================================================
print("="*80)
print("PASO 4: MEDIDAS DE POSICIÓN (TENDENCIA CENTRAL)")
print("="*80)

# Seleccionar variables numéricas para análisis
variables_numericas = ['Edad', 'Calificacion_Matematicas', 'Calificacion_Ciencias', 'Horas_Estudio']

for variable in variables_numericas:
    print(f"\n--- Análisis de: {variable} ---")

    # 4.1 PROMEDIO (Media aritmética)
    promedio = df[variable].mean()
    print(f"Promedio (Media): {promedio:.2f}")
    print(f"  Interpretación: El valor promedio de {variable} es {promedio:.2f}")

    # 4.2 MEDIANA (Percentil 50)
    mediana = df[variable].median()
    print(f"Mediana: {mediana:.2f}")
    print(f"  Interpretación: El 50% de los datos están por debajo de {mediana:.2f}")

    # 4.3 MODA (Valor más frecuente)
    moda = df[variable].mode()
    if len(moda) > 0:
        print(f"Moda: {moda.values[0]:.2f}")
        print(f"  Interpretación: El valor más frecuente es {moda.values[0]:.2f}")

    # 4.4 CUANTILES (Q1, Q2, Q3)
    q1 = df[variable].quantile(0.25)
    q2 = df[variable].quantile(0.50)  # igual a la mediana
    q3 = df[variable].quantile(0.75)

    print(f"Cuartil 1 (Q1 - 25%): {q1:.2f}")
    print(f"  Interpretación: El 25% de los datos están por debajo de {q1:.2f}")
    print(f"Cuartil 2 (Q2 - 50%): {q2:.2f} (igual a la mediana)")
    print(f"Cuartil 3 (Q3 - 75%): {q3:.2f}")
    print(f"  Interpretación: El 75% de los datos están por debajo de {q3:.2f}")

print("\n")

# =============================================================================
# 5. MEDIDAS DE VARIABILIDAD (DISPERSIÓN)
# =============================================================================
print("="*80)
print("PASO 5: MEDIDAS DE VARIABILIDAD (DISPERSIÓN)")
print("="*80)

for variable in variables_numericas:
    print(f"\n--- Análisis de dispersión: {variable} ---")

    # 5.1 MÍNIMO Y MÁXIMO
    minimo = df[variable].min()
    maximo = df[variable].max()
    print(f"Mínimo: {minimo:.2f}")
    print(f"Máximo: {maximo:.2f}")

    # 5.2 RANGO
    rango = maximo - minimo
    print(f"Rango: {rango:.2f}")
    print(f"  Interpretación: La diferencia entre el valor máximo y mínimo es {rango:.2f}")

    # 5.3 VARIANZA
    varianza = df[variable].var()
    print(f"Varianza: {varianza:.2f}")
    print(f"  Interpretación: Medida de dispersión promedio al cuadrado")

    # 5.4 DESVIACIÓN ESTÁNDAR
    desviacion_std = df[variable].std()
    print(f"Desviación Estándar: {desviacion_std:.2f}")
    print(f"  Interpretación: En promedio, los datos se desvían {desviacion_std:.2f} unidades de la media")

    # 5.5 COEFICIENTE DE VARIACIÓN (CV)
    promedio = df[variable].mean()
    coef_variacion = (desviacion_std / promedio) * 100
    print(f"Coeficiente de Variación (CV): {coef_variacion:.2f}%")
    print(f"  Interpretación: La desviación estándar representa el {coef_variacion:.2f}% de la media")
    if coef_variacion < 15:
        print(f"  -> Baja variabilidad (datos homogéneos)")
    elif coef_variacion < 30:
        print(f"  -> Variabilidad moderada")
    else:
        print(f"  -> Alta variabilidad (datos heterogéneos)")

print("\n")

# =============================================================================
# 6. RESUMEN ESTADÍSTICO COMPLETO
# =============================================================================
print("="*80)
print("PASO 6: RESUMEN ESTADÍSTICO COMPLETO")
print("="*80)

print("\nEstadísticas descriptivas de todas las variables numéricas:")
resumen = df[variables_numericas].describe()
print(resumen)
print("\n")

# =============================================================================
# 7. MEDIDAS DE ASOCIACIÓN - CORRELACIÓN DE PEARSON
# =============================================================================
print("="*80)
print("PASO 7: MEDIDAS DE ASOCIACIÓN - CORRELACIÓN DE PEARSON")
print("="*80)

print("\nLa correlación de Pearson mide la relación lineal entre dos variables")
print("Rango: -1 (correlación negativa perfecta) a +1 (correlación positiva perfecta)")
print("Cerca de 0: no hay correlación lineal\n")

# Calcular matriz de correlación de Pearson
matriz_correlacion = df[variables_numericas].corr(method='pearson')

print("Matriz de Correlación de Pearson:")
print(matriz_correlacion)

# Ejemplo específico: correlación entre Matemáticas y Ciencias
correlacion_mat_cie, p_valor = stats.pearsonr(
    df['Calificacion_Matematicas'], 
    df['Calificacion_Ciencias']
)

print(f"\n--- Ejemplo detallado ---")
print(f"Correlación entre Calificación de Matemáticas y Ciencias:")
print(f"Coeficiente de Pearson (r): {correlacion_mat_cie:.4f}")
print(f"P-valor: {p_valor:.6f}")

if p_valor < 0.05:
    print(f"✓ La correlación ES estadísticamente significativa (p < 0.05)")
else:
    print(f"✗ La correlación NO es estadísticamente significativa (p >= 0.05)")

if abs(correlacion_mat_cie) < 0.3:
    print(f"Interpretación: Correlación débil")
elif abs(correlacion_mat_cie) < 0.7:
    print(f"Interpretación: Correlación moderada")
else:
    print(f"Interpretación: Correlación fuerte")

print("\n")

# =============================================================================
# 8. MEDIDAS DE ASOCIACIÓN - RHO DE SPEARMAN
# =============================================================================
print("="*80)
print("PASO 8: MEDIDAS DE ASOCIACIÓN - RHO DE SPEARMAN")
print("="*80)

print("\nRho de Spearman mide la relación monotónica (no necesariamente lineal)")
print("Se basa en rangos ordenados de los datos")
print("Útil cuando los datos no siguen una distribución normal\n")

# Calcular matriz de correlación de Spearman
matriz_spearman = df[variables_numericas].corr(method='spearman')

print("Matriz de Correlación de Spearman:")
print(matriz_spearman)

# Ejemplo específico
spearman_mat_horas, p_valor_sp = stats.spearmanr(
    df['Calificacion_Matematicas'], 
    df['Horas_Estudio']
)

print(f"\n--- Ejemplo detallado ---")
print(f"Correlación entre Calificación de Matemáticas y Horas de Estudio:")
print(f"Coeficiente de Spearman (ρ): {spearman_mat_horas:.4f}")
print(f"P-valor: {p_valor_sp:.6f}")

if p_valor_sp < 0.05:
    print(f"✓ La correlación ES estadísticamente significativa (p < 0.05)")
else:
    print(f"✗ La correlación NO es estadísticamente significativa (p >= 0.05)")

print("\n")

# =============================================================================
# 9. MEDIDAS DE ASOCIACIÓN - CHI-CUADRADO (χ²)
# =============================================================================
print("="*80)
print("PASO 9: MEDIDAS DE ASOCIACIÓN - CHI-CUADRADO (χ²)")
print("="*80)

print("\nChi-cuadrado evalúa la independencia entre variables categóricas")
print("H0: Las variables son independientes")
print("H1: Las variables están asociadas\n")

# Crear tabla de contingencia entre Nivel Socioeconómico y Aprobado
tabla_contingencia = pd.crosstab(
    df['Nivel_Socioeconomico'], 
    df['Aprobado']
)

print("Tabla de Contingencia (Nivel Socioeconómico vs Aprobado):")
print(tabla_contingencia)
print("\n")

# Realizar prueba de Chi-cuadrado
chi2, p_valor_chi, grados_libertad, frecuencias_esperadas = stats.chi2_contingency(tabla_contingencia)

print(f"Resultados de la prueba Chi-cuadrado:")
print(f"Estadístico Chi-cuadrado (χ²): {chi2:.4f}")
print(f"P-valor: {p_valor_chi:.6f}")
print(f"Grados de libertad: {grados_libertad}")

print(f"\nFrecuencias esperadas (si fueran independientes):")
print(pd.DataFrame(
    frecuencias_esperadas, 
    index=tabla_contingencia.index, 
    columns=tabla_contingencia.columns
))

if p_valor_chi < 0.05:
    print(f"\n✓ Rechazamos H0: Las variables SÍ están asociadas (p < 0.05)")
    print(f"  Existe relación entre el Nivel Socioeconómico y Aprobar")
else:
    print(f"\n✗ No rechazamos H0: Las variables son independientes (p >= 0.05)")
    print(f"  No hay evidencia de relación entre Nivel Socioeconómico y Aprobar")

print("\n")

# =============================================================================
# 10. VISUALIZACIONES GRÁFICAS
# =============================================================================
print("="*80)
print("PASO 10: Generando visualizaciones gráficas...")
print("="*80)

# Crear figura con múltiples subgráficas
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
# Añadir línea de tendencia
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

# Guardar la figura
nombre_archivo_graficas = 'analisis_estadistico_completo.png'
plt.savefig(nombre_archivo_graficas, dpi=300, bbox_inches='tight')
print(f"✓ Gráficas guardadas en: {nombre_archivo_graficas}")

# Mostrar las gráficas
plt.show()

print("\n")

# =============================================================================
# 11. TABLA RESUMEN DE TODAS LAS MEDIDAS CALCULADAS
# =============================================================================
print("="*80)
print("PASO 11: TABLA RESUMEN FINAL")
print("="*80)

# Crear un resumen personalizado
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
print("\nRESUMEN ESTADÍSTICO COMPLETO:")
print(resumen_completo.round(2))

# =============================================================================
# 12. EXPORTAR RESULTADOS A EXCEL
# =============================================================================
print("\n")
print("="*80)
print("PASO 12: Exportando resultados a Excel")
print("="*80)

# Crear archivo Excel con múltiples hojas
nombre_archivo_excel = 'resultados_analisis_estadistico.xlsx'

with pd.ExcelWriter(nombre_archivo_excel, engine='openpyxl') as writer:
    # Hoja 1: Datos originales
    df.to_excel(writer, sheet_name='Datos_Originales', index=False)

    # Hoja 2: Resumen estadístico
    resumen_completo.to_excel(writer, sheet_name='Resumen_Estadistico')

    # Hoja 3: Correlación Pearson
    matriz_correlacion.to_excel(writer, sheet_name='Correlacion_Pearson')

    # Hoja 4: Correlación Spearman
    matriz_spearman.to_excel(writer, sheet_name='Correlacion_Spearman')

    # Hoja 5: Tabla de contingencia
    tabla_contingencia.to_excel(writer, sheet_name='Tabla_Contingencia')

print(f"✓ Resultados exportados exitosamente a: {nombre_archivo_excel}")

# =============================================================================
# 13. CONCLUSIONES FINALES
# =============================================================================
print("\n")
print("="*80)
print("CONCLUSIONES DEL ANÁLISIS")
print("="*80)

print("""
Este análisis demostró el uso e interpretación de:

1. MEDIDAS DE POSICIÓN:
   - Media, mediana y moda para identificar el centro de los datos
   - Cuantiles (Q1, Q2, Q3) para entender la distribución

2. MEDIDAS DE VARIABILIDAD:
   - Rango, varianza y desviación estándar para medir dispersión
   - Coeficiente de variación para comparar variabilidad entre variables

3. MEDIDAS DE ASOCIACIÓN:
   - Correlación de Pearson para relaciones lineales entre variables continuas
   - Rho de Spearman para relaciones monotónicas (más robusto)
   - Chi-cuadrado para analizar independencia entre variables categóricas

Las visualizaciones complementan el análisis numérico y facilitan la
interpretación de los resultados.
""")

print("="*80)
print("ANÁLISIS COMPLETADO EXITOSAMENTE")
print("="*80)
print("\nArchivos generados:")
print(f"1. {nombre_archivo_graficas}")
print(f"2. {nombre_archivo_excel}")
print("\n")


# In[ ]:




