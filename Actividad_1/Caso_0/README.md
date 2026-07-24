# Caso 0: Fundamentos y Sintaxis Básica de Python

Este módulo es una guía introductoria y práctica sobre los conceptos elementales de la programación en Python, diseñado para nivel de maestría. Explora la declaración de variables escalares, el comportamiento lógico, operaciones con cadenas de texto y la definición estructurada de funciones personalizadas.

---

## 📚 Temas Académicos Cubiertos

### 1. Variables y Tipado Dinámico
*   Asignación de tipos de datos primitivos en memoria (`int`, `str`, `float`, `bool`).
*   **Sensibilidad a Mayúsculas**: Ilustración de errores comunes de referencia (`NameError`).
*   **Fuerte Tipado**: Python no permite operaciones lógicas o aritméticas implícitas entre tipos incompatibles (como cadenas y enteros), lanzando excepciones `TypeError`.

### 2. Conversión de Tipos (Casting)
*   Uso de funciones integradas como `int()`, `float()`, y `str()`.
*   Análisis de limitaciones de casting, como la conversión de cadenas racionales directamente a enteros, lo cual requiere una conversión intermedia.

### 3. Definición y Modularidad de Funciones (`def`)
*   Firma de funciones con parámetros posicionales.
*   **Tipado Estático (`Type Hinting`)**: Incorporación de tipos de datos en parámetros y retornos (`Union[int, float]`, `str`) para una legibilidad óptima y robustez del código.

---

## 🛠️ Estándares de Calidad Aplicados

*   **Tipado Estático**: Todas las variables principales y las funciones (`funcion_suma` e `iniciales`) cuentan con type annotations nativas de Python.
*   **Manejo Didáctico de Excepciones**: En lugar de permitir que el cuaderno falle silenciosamente o se detenga al ejecutarlo por completo, todos los errores intencionales de la guía han sido capturados con bloques `try-except` explicativos en consola.
