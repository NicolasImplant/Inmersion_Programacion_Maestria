# Actividad Individual 1 - Fundamentos de Programación Científica y Análisis de Datos

Esta carpeta contiene la solución completa, tipada estáticamente y verificada para la **Actividad 1** de la maestría. La actividad aborda desde operaciones básicas de Python hasta el análisis descriptivo y estadístico de datos reales utilizando la librería `pandas`.

---

## 📋 Resumen de Desafíos y Objetivos Pedagógicos

La actividad está estructurada estratégicamente en tres niveles progresivos de dificultad y abstracción:

### 1. Caso 0: Fundamentos y Sintaxis
* **Objetivo**: Evaluar la familiaridad del estudiante con variables básicas, conversiones de tipos y llamadas funcionales elementales.
* **Soluciones**:
  * Registro formal del nombre del estudiante.
  * Operaciones flotantes controladas.
  * Funciones de cálculo sobre longitudes de strings.

### 2. Caso 1: Estructuras de Datos Complejas y Colecciones
* **Objetivo**: Resolver problemas combinando diccionarios indexados de tasas hipotecarias, ordenamiento eficiente y teoría de conjuntos.
* **Soluciones**:
  * Diccionario de 10 entidades bancarias colombianas y cálculo del promedio del mercado (tasas obtenidas del artículo de Forbes).
  * Eliminación de duplicados y ordenación alfabética mediante el algoritmo estable de Timsort ($O(N \log N)$).
  * Resolución matemática precisa de conjuntos basados en el diagrama de Venn `fig/C1_1.png` mediante conectores de intersección ($A \cap B$), unión ($A \cup B$) y diferencia relativa ($B \setminus A$).

### 3. Caso 2: Clasificación de Precios Regionales con Pandas
* **Objetivo**: Diseñar un clasificador dinámico que compare el precio de combustibles de 4,492 estaciones de servicio frente al comportamiento estadístico de su departamento.
* **Soluciones**:
  * Función clasificadora robusta de umbrales múltiples según la variabilidad en desviaciones estándar ($\sigma$) respecto a la media regional ($\bar{p}$).
  * Bucle de clasificación indexado sobre el DataFrame cargado desde la base de datos de Excel (`precios_combustible_dic_2020.xlsx`).
  * Medición de sesgos extremos en los extremos de la distribución (porcentaje de estaciones costosas y baratas).

---

## 🛡️ Soluciones Robustas de Ingeniería

### 💻 Tipado Estático (Type Hinting)
Todas las firmas de las funciones se encuentran anotadas con el módulo `typing` de Python para garantizar la máxima legibilidad de código y consistencia estructural:
```python
from typing import List, Dict, Union

def clasificar_EDS(
    edslist: List[Union[str, float]], 
    promdict: Dict[str, float], 
    desvdict: Dict[str, float]
) -> str:
    ...
```

### ⚙️ Portabilidad Inteligente (Buscador Auto-Sanador)
Para garantizar una experiencia fluida al docente sin importar cómo descargue u organice tus carpetas en su máquina local, se ha diseñado una celda inicial autoejecutable que:
1. **Detecta el entorno físico** y ajusta dinámicamente el directorio de trabajo de Python al directorio donde se encuentra el cuaderno.
2. **Localiza de forma recursiva** el archivo `data/precios_combustible_dic_2020.xlsx` buscando en directorios circundantes o superiores, re-alineando las rutas de pandas.
3. **Instala automáticamente** las dependencias requeridas como `pandas` y `openpyxl` mediante llamadas asíncronas seguras a `pip` si no se encuentran preinstaladas en el entorno.

---

## 📊 Métricas Resultantes Obtenidas

Todas las aserciones incluidas al final del cuaderno de Jupyter han sido ejecutadas de forma local y han arrojado resultados impecables:
* **Promedio Hipotecario General**: `10.625%`
* **Elementos Intersección Conjuntos**: `7` (`{'a', 'b', 'c', 'g', 'h', 'm', 'r'}`)
* **Estaciones Extremadamente Caras (`+++` o `++++`)**: `120 de 4492` ($\approx$ **`2.6714%`**)
* **Estaciones Extremadamente Baratas (`---` o `----`)**: `38 de 4492` ($\approx$ **`0.8459%`**)
