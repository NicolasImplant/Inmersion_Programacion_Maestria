# Caso 1: Estructuras de Datos, Inmutabilidad y Álgebra de Conjuntos en Python

Este módulo aborda de manera profunda el diseño y manipulación de las cuatro estructuras de datos coleccionables nativas de Python (`set`, `list`, `dict` y `tuple`), utilizando un caso de estudio real del sector inmobiliario.

---

## 📚 Temas Académicos Cubiertos

### 1. Conjuntos (`set`) e Intersección Lógica
*   Colecciones no ordenadas de elementos únicos.
*   **Operaciones del Álgebra de Conjuntos**: Cálculo de la intersección lógica (`&` o `.intersection()`) para determinar características comunes entre propiedades inmobiliarias ("Edificio Calasanz" y "Edificio Alcalá"), y de diferencias de conjuntos (`-` o `.difference()`).
*   Evaluación de pertenencia en $O(1)$ constante mediante el operador `in`.

### 2. Listas (`list`) y Anidamiento
*   Colecciones ordenadas, mutables y con elementos duplicados permitidos.
*   Inserción de nuevos elementos (`.append()`), indexación positiva y negativa (indexación invertida), y gestión de colecciones anidadas (ej. listas que contienen otras listas).

### 3. Diccionarios (`dict`) y Estructuras de Datos Complejas
*   Mapeos llave-valor no ordenados para estructurar entidades complejas.
*   Modelado de una base de datos de apartamentos en una estructura anidada del tipo `Dict[str, Dict[str, Any]]`.
*   **Optimización Algorítmica**: Cálculo e iteración automatizada sobre diccionarios complejos para evaluar e identificar la propiedad con menor valor por metro cuadrado ($Valor\_Metro = \frac{Arriendo}{Area}$).

### 4. Tuplas (`tuple`) e Inmutabilidad en Python
*   Colecciones ordenadas e inmutables (read-only) diseñadas para proteger la integridad de los datos en ejecución.
*   Análisis de excepciones `TypeError` y `AttributeError` al intentar mutar una tupla o llamar métodos modificadores inexistentes.

---

## 🛠️ Estándares de Calidad Aplicados

*   **Tipado Estático Estricto**: Configuración de anotaciones de tipo avanzadas (`from typing import Set, List, Dict, Any, Union`) en todas las colecciones para forzar coherencia estructural.
*   **Resolución en Línea (`In-line`)**: Inserción de bloques de código completos y resueltos inmediatamente debajo del enunciado en markdown de cada ejercicio práctico de la guía, facilitando una lectura fluida.
*   **Portabilidad y Manejo de Errores**: Captura didáctica de todas las excepciones intencionales del cuaderno (fuera de límites de listas o alteración de tuplas), garantizando una ejecución secuencial exitosa e ininterrumpida.
