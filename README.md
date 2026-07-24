# Inmersión a la Programación - Maestría en Inteligencia Artificial

Este repositorio contiene las soluciones desarrolladas de manera profesional y académica para las actividades del módulo **Inmersión a la Programación** del programa de Maestría. 

Las soluciones están estructuradas siguiendo las mejores prácticas de la ingeniería de software y la ciencia de datos, utilizando **tipado estático estricto (Type Hinting)**, documentación matemática rigurosa en LaTeX y estrategias avanzadas de portabilidad de datos.

---

## 📂 Estructura del Repositorio

El repositorio se organiza por carpetas lógicas para cada una de las actividades del curso:

```
Inmersion_Programacion_Maestria/ (Raíz del Repositorio)
│
├── README.md                      # Presentación general del curso
│
└── Actividad_1/                   # Módulo de la Actividad Individual 1
    ├── README.md                  # Documentación técnica de la Actividad 1
    ├── U1_Actividad.ipynb         # Cuaderno de Jupyter con las soluciones completas
    ├── data/                      # Base de datos regional de precios de combustible
    └── fig/                       # Diagramas y recursos visuales de los enunciados
```

---

## 🛠️ Estándares Técnicos Aplicados

* **Tipado Estático Riguroso**: Todas las funciones y asignaciones del código de soluciones incorporan anotaciones de tipo nativas y del módulo `typing` de Python para garantizar claridad estructural, autocompletado avanzado y robustez de análisis estático.
* **Auto-Alineación y Portabilidad Universal (Opción A)**: El cuaderno cuenta con un bloque de inicialización inteligente que detecta su propia ruta física, comprueba y auto-instala dependencias faltantes (como `pandas` y `openpyxl`), y realiza búsquedas recursivas en disco de los datasets para evitar errores `FileNotFoundError` en la máquina del revisor o profesor.
* **Documentación Académica**: Explicación formal de los conceptos matemáticos (unión de conjuntos, Timsort, desviación estándar, umbrales de distribución normal) formateados con ecuaciones en LaTeX dentro del cuaderno.

---

## 🚀 Cómo Ejecutar los Cuadernos

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/NicolasImplant/Inmersion_Programacion_Maestria.git
   ```
2. **Navegar a la actividad deseada**:
   ```bash
   cd Actividad_1
   ```
3. **Iniciar el servidor de Jupyter** o ejecutar directamente en un entorno compatible (JupyterLab, VS Code, Deepnote, etc.):
   ```bash
   jupyter notebook U1_Actividad.ipynb
   ```

*Nota: La celda número 0 se encargará de configurar de forma transparente las dependencias e indexar las bases de datos para garantizar una ejecución impecable de principio a fin.*
