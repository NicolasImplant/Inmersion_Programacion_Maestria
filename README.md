# Inmersión a la Programación — Actividad 1
**Maestría en Inteligencia Artificial y Ciencia de Datos**  
**Estudiante:** Juan Nicolas Patiño Rodriguez  
**Docente:** Profesor Evaluador  

---

## 🎯 Resumen de la Actividad

Esta entrega contiene la resolución completa, optimizada y documentada de la **Actividad 1** del módulo *Inmersión a la Programación*. Consiste en tres casos de estudio tutoriales independientes que abordan desde los fundamentos de la sintaxis en Python hasta la manipulación avanzada de bases de datos utilizando Pandas, junto con un cuaderno unificado que integra todos los conceptos prácticos.

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
└── README.md                    # Este archivo: Guía de navegación general
```

---

## 🌟 Estándares Premium de Implementación

Para asegurar un nivel de excelencia académica de maestría, se aplicaron de forma rigurosa las siguientes directrices en todos los cuadernos:

1.  **Tipado Estático Estricto (`Static Typing`)**:
    *   Uso exhaustivo de anotaciones de tipo nativas (`from typing import Set, List, Dict, Any, Union, Optional`) en todas las variables, listas de contacto, diccionarios anidados de propiedades y firmas de funciones matemáticas.
2.  **Portabilidad Auto-Sanadora Universal (Opción A)**:
    *   Inyección de un bloque dinámico al inicio de los cuadernos que localiza recursivamente la ubicación física de las bases de datos de combustibles (.xlsx) y auto-instala dependencias esenciales (`pandas`, `openpyxl`) si faltan, garantizando que el profesor pueda ejecutar con un solo clic de "Run All" en cualquier máquina sin necesidad de configurar rutas de red fijas o terminales.
3.  **Manejo Pedagógico de Errores e Inmutabilidad**:
    *   Todas las celdas diseñadas para lanzar errores con fines académicos (`NameError`, `TypeError`, `ValueError`, `IndexError`, `AttributeError`) fueron envueltas de manera controlada en bloques estructurados `try/except`. Al ejecutarse, capturan el error esperado e imprimen una explicación detallada en español sobre la causa del error en memoria y su corrección.
4.  **Resolución Integrada en Línea (`In-line`)**:
    *   Las soluciones de cada ejercicio práctico fueron insertadas directamente debajo de sus respectivos enunciados en el cuerpo de los cuadernos, evitando desplazamientos innecesarios y garantizando una experiencia interactiva fluida.

---

## 🧪 Validación y Verificación

Todos los cuadernos han sido verificados secuencialmente de principio a fin, garantizando **0 excepciones no controladas** y un comportamiento perfecto.

Para reproducir la validación general de todo el repositorio, ejecute en su terminal:
```bash
python Actividad_1/scratch/execute_all_cases.py
```

*Este script ejecutará secuencialmente cada uno de los cuadernos, cargará las bases de datos dinámicamente y certificará la ausencia de fallas en ejecución.*
