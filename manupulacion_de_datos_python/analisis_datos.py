import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Usando el backend Agg que no requiere GUI
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF
import numpy as np

# Configuración de estilo para las gráficas
plt.style.use('default')  # Usando el estilo por defecto
sns.set_style("whitegrid")  # Usando el estilo de seaborn

def analizar_caso_1():
    print("\n=== ANÁLISIS DEL CASO 1 ===")
    # Cargar datos
    df = pd.read_csv('data.csv')
    
    # Mostrar primeros registros
    print("\nPrimeros registros:")
    print(df.head())
    
    # Identificar valores nulos
    print("\nValores nulos por columna:")
    print(df.isnull().sum())
    
    # Identificar registros duplicados
    print("\nRegistros duplicados:")
    print(df.duplicated().sum())
    
    # Eliminar duplicados
    df = df.drop_duplicates()
    
    # Rellenar valores nulos
    df['Edad'] = df['Edad'].fillna(df['Edad'].mean())
    df['Puntaje'] = df['Puntaje'].fillna(df['Puntaje'].mean())
    
    # Crear gráficas
    plt.figure(figsize=(15, 10))
    
    # Gráfica 1: Distribución de edades
    plt.subplot(2, 2, 1)
    sns.histplot(data=df, x='Edad', bins=10, kde=True)
    plt.title('Distribución de Edades')
    plt.xlabel('Edad')
    plt.ylabel('Frecuencia')
    
    # Gráfica 2: Puntaje promedio por país
    plt.subplot(2, 2, 2)
    df.groupby('Pais')['Puntaje'].mean().sort_values().plot(kind='barh')
    plt.title('Puntaje Promedio por País')
    plt.xlabel('Puntaje Promedio')
    plt.ylabel('País')
    
    # Gráfica 3: Distribución por género
    plt.subplot(2, 2, 3)
    df['Genero'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'pink'])
    plt.title('Distribución por Género')
    
    plt.tight_layout()
    plt.savefig('caso1_graficas.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return df

def analizar_caso_2():
    print("\n=== ANÁLISIS DEL CASO 2 ===")
    # Cargar datos
    df = pd.read_csv('ventas.csv')
    
    # Mostrar primeros registros
    print("\nPrimeros registros:")
    print(df.head())
    
    # Identificar valores nulos
    print("\nValores nulos por columna:")
    print(df.isnull().sum())
    
    # Identificar registros duplicados
    print("\nRegistros duplicados:")
    print(df.duplicated().sum())
    
    # Crear gráficas
    plt.figure(figsize=(15, 10))
    
    # Gráfica 1: Ventas por región
    plt.subplot(2, 2, 1)
    ventas_region = df.groupby('Region')['Cantidad'].sum().sort_values()
    sns.barplot(x=ventas_region.index, y=ventas_region.values)
    plt.title('Ventas por Región')
    plt.xlabel('Región')
    plt.ylabel('Cantidad Total')
    
    # Gráfica 2: Distribución por categoría
    plt.subplot(2, 2, 2)
    df['Categoria'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette("pastel"))
    plt.title('Distribución por Categoría')
    
    # Gráfica 3: Distribución de precios
    plt.subplot(2, 2, 3)
    sns.boxplot(data=df, x='Categoria', y='Precio')
    plt.title('Distribución de Precios por Categoría')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.savefig('caso2_graficas.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return df

def analizar_caso_3():
    print("\n=== ANÁLISIS DEL CASO 3 ===")
    # Cargar datos
    df = pd.read_csv('salud.csv')
    
    # Mostrar primeros registros
    print("\nPrimeros registros:")
    print(df.head())
    
    # Identificar valores nulos
    print("\nValores nulos por columna:")
    print(df.isnull().sum())
    
    # Identificar registros duplicados
    print("\nRegistros duplicados:")
    print(df.duplicated().sum())
    
    # Crear gráficas
    plt.figure(figsize=(15, 10))
    
    # Gráfica 1: Presión arterial por región
    plt.subplot(2, 2, 1)
    df['Presion_Arterial'] = df['Presion_Arterial'].str.split('/').str[0].astype(float)
    sns.barplot(data=df, x='Region', y='Presion_Arterial', ci=None)
    plt.title('Presión Arterial Promedio por Región')
    plt.xlabel('Región')
    plt.ylabel('Presión Arterial Sistólica')
    
    # Gráfica 2: Distribución por género
    plt.subplot(2, 2, 2)
    df['Genero'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'pink'])
    plt.title('Distribución por Género')
    
    # Gráfica 3: Distribución de edades
    plt.subplot(2, 2, 3)
    sns.histplot(data=df, x='Edad', bins=10, kde=True)
    plt.title('Distribución de Edades')
    plt.xlabel('Edad')
    plt.ylabel('Frecuencia')
    
    plt.tight_layout()
    plt.savefig('caso3_graficas.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return df

def generar_informe():
    pdf = FPDF()
    pdf.add_page()
    
    # Título
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, "Análisis de Datos - Casos de Estudio", ln=True, align='C')
    pdf.ln(10)
    
    # Caso 1
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, "Caso 1: Análisis de Datos Personales", ln=True)
    pdf.image('caso1_graficas.png', x=10, y=40, w=190)
    pdf.ln(120)
    
    # Caso 2
    pdf.add_page()
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, "Caso 2: Análisis de Ventas", ln=True)
    pdf.image('caso2_graficas.png', x=10, y=30, w=190)
    pdf.ln(120)
    
    # Caso 3
    pdf.add_page()
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, "Caso 3: Análisis de Datos de Salud", ln=True)
    pdf.image('caso3_graficas.png', x=10, y=30, w=190)
    
    pdf.output("analisis_datos.pdf")

def main():
    # Analizar los tres casos
    df1 = analizar_caso_1()
    df2 = analizar_caso_2()
    df3 = analizar_caso_3()
    
    # Generar informe PDF
    generar_informe()
    
    print("\nAnálisis completado. Se ha generado el archivo 'analisis_datos.pdf'")

if __name__ == "__main__":
    main() 