# Inmersión a la Programación
**Maestría en Inteligencia Artificial**  
**Estudiante:** Juan Nicolas Patiño Rodriguez  
**Docente:** Profesor Evaluador  

---

## 🎯 Resumen del Repositorio

Este repositorio reúne las entregas resueltas, optimizadas y documentadas del módulo
*Inmersión a la Programación*, una por unidad:

- **[Actividad 1](Actividad_1/README.md)** — Fundamentos de Python: tres casos de estudio
  tutoriales (sintaxis, estructuras de datos, control de flujo y Pandas) más un cuaderno
  individual unificado (`U1_Actividad.ipynb`).
- **[Actividad 2](Actividad_2/README.md)** — Carga y visualización de datos con Python:
  análisis, descomposición de series de tiempo y pronóstico SARIMA sobre un histórico de
  temperaturas, entregado como informe científico en LaTeX/PDF.

---

## 📂 Estructura del Repositorio

El repositorio se organiza de forma lógica, modular y académica:

```text
Inmersion_Programacion_Maestria/
├── Actividad_1/
│   ├── U1_Actividad.ipynb       # Cuaderno unificado completo y verificado
│   ├── Caso_0/                  # Caso 0: Introducción, tipos de datos y excepciones
│   │   ├── Caso_0.ipynb         # Cuaderno interactivo resuelto
│   │   └── README.md            # Documentación académica del Caso 0
│   ├── Caso_1/                  # Caso 1: Estructuras de datos, conjuntos y diccionarios
│   │   ├── Caso_1.ipynb         # Cuaderno interactivo resuelto
│   │   ├── fig/                 # Diagramas y recursos gráficos del Caso 1
│   │   └── README.md            # Documentación académica del Caso 1
│   ├── Caso_2/                  # Caso 2: Control de flujo, Pandas y clasificación
│   │   ├── Caso_2.ipynb         # Cuaderno interactivo resuelto
│   │   ├── data/                # Bases de datos de precios de combustible (.xlsx)
│   │   ├── fig/                 # Diagramas y recursos de apoyo del Caso 2
│   │   └── README.md            # Documentación académica del Caso 2
│   └── scratch/                 # Scripts automatizados de desarrollo y validación
│       ├── copy_cases.py        # Migrador de carpetas del workspace al repo
│       ├── apply_solutions_*.py # Aplicadores programáticos de tipado y soluciones
│       ├── execute_case_*.py    # Validadores de ejecución individuales
│       └── execute_all_cases.py # Validador integral de todo el proyecto
├── Actividad_2/
│   ├── README.md                # Documentación académica de la Actividad 2
│   ├── requirements.txt         # Dependencias fijadas del entorno (.venv/)
│   ├── pyproject.toml           # Configuración de mypy --strict
│   ├── data/                    # Dataset fuente (temperaturas históricas, 100 ciudades)
│   ├── src/                     # Pipeline de análisis tipado (carga, EDA, descomposición, SARIMA)
│   └── report/                  # Informe científico en LaTeX (main.tex, sections/, figures/, main.pdf)
└── README.md                    # Este archivo: Guía de navegación general
```

---

## 🌟 Estándares de Implementación

Para asegurar un nivel de excelencia académica de maestría, se aplicaron de forma rigurosa
las siguientes directrices, adaptadas al formato de entrega de cada actividad.

### Actividad 1 (cuadernos Jupyter)

1.  **Tipado Estático Estricto (`Static Typing`)**:
    *   Uso exhaustivo de anotaciones de tipo nativas (`from typing import Set, List, Dict, Any, Union, Optional`) en todas las variables, listas de contacto, diccionarios anidados de propiedades y firmas de funciones matemáticas.
2.  **Portabilidad Auto-Sanadora Universal (Opción A)**:
    *   Inyección de un bloque dinámico al inicio de los cuadernos que localiza recursivamente la ubicación física de las bases de datos de combustibles (.xlsx) y auto-instala dependencias esenciales (`pandas`, `openpyxl`) si faltan, garantizando que el profesor pueda ejecutar con un solo clic de "Run All" en cualquier máquina sin necesidad de configurar rutas de red fijas o terminales.
3.  **Manejo Pedagógico de Errores e Inmutabilidad**:
    *   Todas las celdas diseñadas para lanzar errores con fines académicos (`NameError`, `TypeError`, `ValueError`, `IndexError`, `AttributeError`) fueron envueltas de manera controlada en bloques estructurados `try/except`. Al ejecutarse, capturan el error esperado e imprimen una explicación detallada en español sobre la causa del error en memoria y su corrección.
4.  **Resolución Integrada en Línea (`In-line`)**:
    *   Las soluciones de cada ejercicio práctico fueron insertadas directamente debajo de sus respectivos enunciados en el cuerpo de los cuadernos, evitando desplazamientos innecesarios y garantizando una experiencia interactiva fluida.

### Actividad 2 (pipeline Python + informe LaTeX)

1.  **Tipado Estático Estricto verificado con herramientas**:
    *   Todo `src/` pasa `mypy --strict` (configurado en `pyproject.toml`), en lugar de depender solo de la disciplina del autor.
2.  **Pipeline reproducible de un solo comando**:
    *   `python src/run_pipeline.py` regenera de forma determinística las 7 figuras del informe y `report/macros.tex` a partir de los datos crudos.
3.  **Una única fuente de verdad para los resultados**:
    *   Cada estadística citada en el informe (media, RMSE, orden del modelo SARIMA, p-valor ADF, etc.) se calcula en Python y se expone como comandos LaTeX (`\newcommand`) en `report/macros.tex`, en vez de transcribirse manualmente.
4.  **Decisiones metodológicas basadas en evidencia**:
    *   Se identificó y documentó un vacío de 20 años en los datos de Bogotá, acotando la ventana de análisis en lugar de interpolar sobre él.
5.  **Informe con estándares de documento científico**:
    *   LaTeX con citas bibliográficas (`natbib`), figuras vectoriales referenciadas, y notación numérica en convención española.

Ver el detalle completo de cada actividad en sus respectivos README:
[Actividad 1](Actividad_1/README.md) · [Actividad 2](Actividad_2/README.md).

---

## 🧪 Validación y Verificación

**Actividad 1**: todos los cuadernos han sido verificados secuencialmente de principio a
fin, garantizando **0 excepciones no controladas**. Para reproducir la validación:
```bash
python Actividad_1/scratch/execute_all_cases.py
```
*Este script ejecutará secuencialmente cada uno de los cuadernos, cargará las bases de datos dinámicamente y certificará la ausencia de fallas en ejecución.*

**Actividad 2**: el pipeline de análisis corre de punta a punta sin excepciones y `mypy
--strict` no reporta errores. Para reproducir la validación y compilar el informe:
```bash
cd Actividad_2
./.venv/Scripts/python -m mypy
./.venv/Scripts/python src/run_pipeline.py
cd report && latexmk -pdf main.tex
```
*Ver [Actividad_2/README.md](Actividad_2/README.md) para instrucciones completas de configuración del entorno.*
