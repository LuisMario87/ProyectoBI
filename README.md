# ProyectiBI
# Proyecto de Analítica de Datos y Business Intelligence — Caso Farmacia

## 📌 Descripción
Este proyecto aplica técnicas de **Analítica de Datos y Business Intelligence (BI)** a un dataset de ventas farmacéuticas (30,000 registros).
El objetivo es desarrollar un pipeline reproducible en **Python** para la limpieza, modelado y análisis de datos, además de dashboards con KPIs accionables.

## 🎯 Objetivos
- Implementar un pipeline ETL reproducible para el dataset farmacéutico.
- Definir y calcular KPIs relevantes para el negocio.
- Construir dashboards con narrativa ejecutiva.
- Documentar resultados y visualizaciones en reportes y notebooks.

## 📂 Estructura del repositorio
repo_proyecto_farmacia/
│
├── data/
│ ├── raw/ # Dataset original (no incluido aquí por privacidad)
│ └── processed/ # Dataset procesado de muestra
│
├── scripts/
│ └── etl_preliminar.py # Script ETL inicial
│
├── notebooks/
│ └── exploracion_inicial.ipynb # Notebook de exploración y visualización
│
├── report/
│ └── Entregable_Intermedio_Farmacia.docx # Documento intermedio (Word)
│
└── README.md


## ⚙️ Requisitos
- Python 3.9+
- Bibliotecas:
  - pandas
  - numpy
  - matplotlib
  - openpyxl (para Excel)

Instalación rápida:
```bash
pip install pandas numpy matplotlib openpyxl
