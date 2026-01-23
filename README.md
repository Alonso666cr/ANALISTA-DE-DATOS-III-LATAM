# ANALISTA-DE-DATOS-III-LATAM
Ejemplo práctico de lo que se solicita, conozca un ANALISTA DE DATOS III de una importante entidad financiera privada en Costa Rica [23-01-2026].

# PROYECTO DE ANÁLISIS ESTADÍSTICO DESCRIPTIVO

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

## Descripción
Este proyecto ejemplifica el uso e interpretación de las principales medidas estadísticas:
- **Medidas de posición**: Promedio, mediana, moda, cuantiles
- **Medidas de variabilidad**: Rango, mínimo, máximo, varianza, desviación estándar, coeficiente de variación
- **Medidas de asociación**: Correlación de Pearson, Chi-cuadrado, Rho de Spearman

## Contenido del Proyecto
- `estudiantes_datos.csv` - Dataset con 50 estudiantes y sus calificaciones
- `analisis_estadistico.py` - Script principal con todo el análisis
- `README.md` - Este archivo con instrucciones

## Requisitos

### Librerías de Python necesarias:
```bash
pip install pandas numpy matplotlib seaborn scipy openpyxl
```

### Versiones recomendadas:
- Python 3.8 o superior
- pandas >= 1.3.0
- numpy >= 1.21.0
- matplotlib >= 3.4.0
- seaborn >= 0.11.0
- scipy >= 1.7.0
- openpyxl >= 3.0.0

## Instalación en Anaconda

### Opción 1: Instalar librerías individualmente
```bash
conda install pandas numpy matplotlib seaborn scipy
conda install -c anaconda openpyxl
```

### Opción 2: Crear un entorno nuevo (recomendado)
```bash
# Crear entorno
conda create -n estadistica python=3.10

# Activar entorno
conda activate estadistica

# Instalar librerías
conda install pandas numpy matplotlib seaborn scipy
conda install -c anaconda openpyxl
```

## Uso

### Paso 1: Preparar los archivos
Asegúrate de tener ambos archivos en la misma carpeta:
- `estudiantes_datos.csv`
- `analisis_estadistico.py`

### Paso 2: Ejecutar el análisis

#### Desde Anaconda Navigator:
1. Abre Anaconda Navigator
2. Lanza Jupyter Notebook o Spyder
3. Navega a la carpeta donde guardaste los archivos
4. Abre y ejecuta `analisis_estadistico.py`

#### Desde la terminal/línea de comandos:
```bash
# Navega a la carpeta del proyecto
cd ruta/a/tu/carpeta

# Ejecuta el script
python analisis_estadistico.py
```

#### Desde Spyder (IDE de Anaconda):
1. Abre Spyder
2. Abre el archivo `analisis_estadistico.py`
3. Presiona F5 o el botón "Run"

## Salidas del Programa

El script genera automáticamente:

1. **Salida en consola**: Todos los cálculos estadísticos con interpretaciones
2. **Gráficas**: Archivo `analisis_estadistico_completo.png` con 9 visualizaciones
3. **Excel**: Archivo `resultados_analisis_estadistico.xlsx` con 5 hojas:
   - Datos originales
   - Resumen estadístico
   - Correlación de Pearson
   - Correlación de Spearman
   - Tabla de contingencia

## Estructura del Análisis

### 1. Medidas de Posición
- **Promedio (Media)**: Valor central de los datos
- **Mediana**: Valor que divide los datos en dos partes iguales
- **Moda**: Valor más frecuente
- **Cuantiles**: Q1 (25%), Q2 (50%), Q3 (75%)

### 2. Medidas de Variabilidad
- **Rango**: Diferencia entre máximo y mínimo
- **Varianza**: Promedio de las desviaciones al cuadrado
- **Desviación Estándar**: Raíz cuadrada de la varianza
- **Coeficiente de Variación**: Desviación estándar relativa a la media (%)

### 3. Medidas de Asociación
- **Correlación de Pearson**: Relación lineal entre variables continuas (-1 a +1)
- **Rho de Spearman**: Correlación basada en rangos (más robusta)
- **Chi-cuadrado**: Independencia entre variables categóricas

## Visualizaciones Generadas

1. **Histograma**: Distribución de calificaciones de matemáticas
2. **Box Plot**: Comparación de calificaciones
3. **Scatter Plot**: Correlación matemáticas vs ciencias
4. **Histograma**: Distribución de horas de estudio
5. **Mapa de Calor**: Correlación de Pearson
6. **Scatter Plot**: Horas de estudio vs calificación
7. **Gráfico de Barras**: Aprobados por nivel socioeconómico
8. **Violin Plot**: Distribución por estado de aprobación
9. **Mapa de Calor**: Correlación de Spearman

## Dataset

El archivo `estudiantes_datos.csv` contiene 50 registros con las siguientes variables:

### Variables incluidas:
- **Estudiante**: Nombre del estudiante
- **Edad**: 18-20 años
- **Calificacion_Matematicas**: Puntuación 54-95
- **Calificacion_Ciencias**: Puntuación 56-95
- **Horas_Estudio**: 1-8 horas semanales
- **Nivel_Socioeconomico**: Alto, Medio, Bajo
- **Aprobado**: Si/No

## Personalización

### Usar tu propio dataset:
1. Prepara un archivo CSV o Excel con tus datos
2. Modifica la línea 39 del script:
   ```python
   ruta_archivo = 'tu_archivo.csv'  # o 'tu_archivo.xlsx'
   ```
3. Ajusta los nombres de las columnas en las líneas 61 y siguientes

### Cambiar variables a analizar:
Modifica la lista en la línea 61:
```python
variables_numericas = ['Variable1', 'Variable2', 'Variable3']
```

## Solución de Problemas

### Error: "ModuleNotFoundError"
- Instala la librería faltante: `pip install nombre_libreria`

### Error: "FileNotFoundError"
- Verifica que el archivo CSV esté en la misma carpeta que el script
- O especifica la ruta completa: `ruta_archivo = 'C:/Users/TuNombre/carpeta/archivo.csv'`

### Las gráficas no se muestran:
- En Jupyter: Agrega `%matplotlib inline` al inicio
- En scripts: Asegúrate de que `plt.show()` esté presente

### Excel no se exporta:
- Instala openpyxl: `pip install openpyxl`

## Contacto y Soporte

Este proyecto fue creado como demostración de análisis estadístico descriptivo.

**Autor**: Apache  
**Fecha**: Enero 2026  
**Propósito**: Aplicación a oferta de empleo - Análisis Estadístico

---

## Notas Adicionales

- El código está completamente comentado para facilitar la comprensión
- Se utilizan solo funciones básicas de Python (código secuencial)
- Todas las interpretaciones están incluidas en la salida
- El análisis es reproducible y puede adaptarse a otros datasets

¡Buena suerte con tu aplicación! 🚀

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

**Atribución requerida**: Si usas, modificas o distribuyes este código, por favor mantén la atribución del autor original (Apache) en cualquier trabajo derivado o documentación.

## 👤 Autor

**Apache**
- 🎓 Estudiante de Maestría en Matemáticas Aplicadas y Ciencias de la Computación
- 🏫 Universidad del Rosario, Colombia
- 💼 17+ años de experiencia en TI y Arquitectura Empresarial
- 🎯 Especialización en IA y Machine Learning

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## ⭐ Si te resulta útil

Si este proyecto te ayuda en tu aprendizaje o trabajo, considera darle una ⭐ en GitHub.

## 📧 Contacto

Para preguntas, sugerencias o colaboraciones, puedes abrir un issue en GitHub.
