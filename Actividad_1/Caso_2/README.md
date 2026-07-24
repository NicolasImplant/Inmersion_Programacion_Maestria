# Caso 2: Control de Flujo, Pandas y Clasificación de Datos en Python

Este módulo es una guía práctica-tutorial que profundiza en las estructuras de control de flujo condicional (`if/elif/else`), ciclos repetitivos (`for`), y la manipulación de dataframes utilizando la biblioteca de análisis de datos **Pandas** para resolver un caso de estudio real sobre la clasificación de Estaciones de Servicio (EDS) en Colombia.

---

## 📚 Temas Académicos Cubiertos

### 1. Control de Flujo y Toma de Decisiones
*   Uso estructurado de operadores de comparación e identidades lógicas (`&`, `|`, `in`).
*   Diseño de algoritmos de decisión ramificados para resolver problemas matemáticos clásicos (ej. divisibilidad y números pares/impares).

### 2. Ciclos Repetitivos y Generadores (`for` y `range`)
*   Uso de iteradores indexados para acumulación de sumas y productorias secuenciales (cálculo de factorial de $N$).
*   Filtrado aritmético condicional dentro de bucles en grandes espacios de búsqueda (identificación de múltiplos de 2 y de 3 que no son múltiplos de 5 en un rango de 1 a 1000).

### 3. Introducción Práctica a Pandas
*   Carga robusta de archivos de Excel utilizando `pd.read_excel()` con soporte de motor `openpyxl`.
*   Navegación e inspección del dataframe: lectura de dimensiones, índices (`.index`), columnas (`.columns`), tipos de datos (`.dtypes`) e indexación explícita mediante `.loc[]`.
*   Análisis de frecuencia estadística de variables categóricas mediante `.value_counts()`.

### 4. Algoritmos de Clasificación Regional de Precios
*   Modelado de la función `clasificar_EDS()` para categorizar estaciones según la distribución regional de precios (Gasolina y Diesel) utilizando promedios estadísticos ($\mu$) y desviaciones estándar ($\sigma$).

---

## 🛠️ Estándares de Calidad Aplicados

*   **Portabilidad Auto-Sanadora (Opción A)**: Inyección de un bloque dinámico en la Celda 0 que verifica e instala de forma automática dependencias críticas (`pandas`, `openpyxl`) y localiza de manera recursiva el dataset `precios_combustible_dic_2020.xlsx` sin importar el directorio activo de ejecución.
*   **Tipado Estático Estricto**: Firma de funciones y variables anotadas con tipos estáticos explícitos, maximizando la legibilidad y mantenimiento del código bajo estándares profesionales.
*   **Corrección de Consistencia**: Identificación y corrección de inconsistencias en las etiquetas del cuaderno (corrigiendo la duplicación de "Ejercicio 3" a "Ejercicio 4") e inyección de soluciones detalladas en línea.
