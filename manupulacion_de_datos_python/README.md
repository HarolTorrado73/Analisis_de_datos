# Análisis de Datos - Casos de Estudio

Este proyecto contiene tres casos de estudio para el análisis de datos utilizando Python.

## Casos de Estudio

1. **Caso 1: Datos Personales**
   - Análisis de datos demográficos
   - Distribución de edades y puntajes
   - Análisis por país y género

2. **Caso 2: Ventas**
   - Análisis de ventas por región
   - Distribución por categoría de productos
   - Análisis de precios

3. **Caso 3: Salud**
   - Análisis de datos de salud
   - Presión arterial por región
   - Distribución por género y edad

## Requisitos

- Python 3.8 o superior
- Dependencias listadas en `requirements.txt`

## Instalación

1. Clonar el repositorio
2. Crear un entorno virtual (opcional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Asegúrate de que los archivos CSV estén en el directorio raíz:
   - `data.csv`
   - `ventas.csv`
   - `salud.csv`

2. Ejecutar el script de análisis:
   ```bash
   python analisis_datos.py
   ```

3. El script generará:
   - Gráficas para cada caso de estudio
   - Un archivo PDF con el análisis completo

## Estructura del Proyecto

```
.
├── README.md
├── requirements.txt
├── analisis_datos.py
├── data.csv
├── ventas.csv
├── salud.csv
├── caso1_graficas.png
├── caso2_graficas.png
├── caso3_graficas.png
└── analisis_datos.pdf
```

## Resultados

El script generará un archivo PDF (`analisis_datos.pdf`) que contiene:
- Gráficas de cada caso de estudio
- Análisis estadístico
- Conclusiones principales 