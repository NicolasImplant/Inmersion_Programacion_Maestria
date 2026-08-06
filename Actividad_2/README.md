# Actividad 2: Cargando y Visualizando Datos con Python — Series de Tiempo

**Maestría en Inteligencia Artificial y Ciencia de Datos**
**Estudiante:** Juan Nicolás Patiño Rodríguez

---

## 🎯 Resumen de la Actividad

Esta entrega resuelve la actividad evaluativa "Problema" de la Unidad 2: un análisis del
histórico de temperatura promedio mensual de 100 ciudades del mundo (dataset derivado de
Berkeley Earth), con foco en Bogotá. El entregable final es un **informe científico en
LaTeX/PDF** que cubre análisis gráfico, descomposición de la serie de tiempo y pronóstico
mediante un modelo SARIMA, siguiendo la rúbrica de la Guía de Actividades UA2.

A diferencia de los Casos 3–5 (notebooks tutoriales con ejercicios guiados sobre TRM/IPC y
precipitaciones, aún pendientes de resolución), este directorio contiene el pipeline de
análisis y el informe correspondientes a la actividad calificada.

---

## 📂 Estructura del Directorio

```text
Actividad_2/
├── requirements.txt          # Dependencias fijadas del entorno (.venv/)
├── pyproject.toml            # Configuracion de mypy --strict
├── data/
│   └── Actividad_2_Data.csv  # Dataset fuente (temperaturas historicas, 100 ciudades)
├── src/                      # Pipeline de analisis, tipado estatico estricto
│   ├── data_loading.py       # Carga, limpieza y series por ciudad
│   ├── eda.py                 # Analisis grafico comparativo (EDA)
│   ├── decomposition.py       # Descomposicion aditiva (tendencia/estacionalidad/residuo)
│   ├── forecasting.py         # ADF, ACF/PACF, seleccion de orden SARIMA, pronostico
│   └── run_pipeline.py        # Orquestador: regenera figuras y report/macros.tex
└── report/                   # Informe cientifico en LaTeX
    ├── main.tex               # Documento maestro
    ├── references.bib         # Bibliografia
    ├── macros.tex              # Resultados numericos (generado por run_pipeline.py)
    ├── sections/               # Una seccion por archivo (introduccion...conclusiones)
    ├── figures/                 # Figuras generadas por el pipeline (PDF vectorial)
    └── main.pdf                 # Informe compilado (entregable)
```

---

## 🌟 Estándares Aplicados

1. **Tipado estático estricto**: todo `src/` pasa `mypy --strict` (configurado en
   `pyproject.toml`), con anotaciones explícitas en funciones, variables y estructuras de
   datos (`dataclass` para resultados de partición train/test, orden SARIMA y pronósticos).
2. **Pipeline reproducible de un solo comando**: `python src/run_pipeline.py` ejecuta de
   punta a punta la carga de datos, el análisis gráfico, la descomposición y el modelado,
   regenerando de forma determinística las 7 figuras del informe y `report/macros.tex`.
3. **Una única fuente de verdad para los números del informe**: cada estadística citada en
   el texto (media, RMSE, orden del modelo, p-valor de la prueba ADF, etc.) se calcula en
   Python y se expone como un comando LaTeX (`\newcommand`) en `report/macros.tex`, evitando
   transcribir manualmente resultados que podrían quedar desactualizados.
4. **Decisiones metodológicas basadas en evidencia**: se identificó un vacío de 20 años en
   los datos de Bogotá (1830–1850) mediante inspección de la descomposición, y se acotó la
   ventana de análisis a 1851–2013 en lugar de interpolar sobre el vacío, documentando esta
   decisión tanto en el código (`data_loading.load_city_series(..., start=...)`) como en el
   informe.
5. **Informe con estándares de documento científico**: LaTeX con clase `article`, citas
   bibliográficas via `natbib`, figuras vectoriales referenciadas con `\ref`, y notación
   numérica consistente con la convención española (separador decimal `,`, separador de
   miles `.`).

---

## 🧪 Reproducción

```bash
cd Actividad_2
python -m venv .venv
./.venv/Scripts/pip install -r requirements.txt   # Windows; usar bin/pip en Unix

# Verificacion de tipado estricto
./.venv/Scripts/python -m mypy

# Pipeline de analisis: regenera report/figures/*.pdf y report/macros.tex
./.venv/Scripts/python src/run_pipeline.py

# Compilacion del informe (requiere una distribucion LaTeX con latexmk, p. ej. MiKTeX o TeX Live)
cd report
latexmk -pdf main.tex
```
