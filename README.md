# Pipeline de Datos - Ingesta Automatizada

## Descripción del Proyecto
Este proyecto implementa el primer paso funcional de un pipeline de datos: la automatización de la ingesta desde una fuente de origen hacia una estructura organizada de almacenamiento inicial.

## Fuente de Datos
Se utilizó un dataset estructurado en formato CSV (`riesgo_hipertension_dataset.csv`) que contiene datos de pacientes para evaluar el riesgo de hipertensión.

## Arquitectura y Estructura de Carpetas
El proyecto sigue buenas prácticas de estructuración:
* `data/source/`: Contiene los datos crudos originales.
* `data/raw/`: Almacenamiento inicial organizado donde llegan los datos ingeridos.
* `src/`: Contiene el script de automatización.

## Herramientas y Ejecución
Se utilizó Python con control de errores (`try-except`) y librerías estándar (`os`, `shutil`, `logging`, `datetime`).

**Pasos para ejecutar:**
1. Navegar a la carpeta `src/`.
2. Ejecutar el script: `python ingesta_automatizada.py`.
3. Revisar la carpeta `data/raw/` para confirmar la creación del archivo con su timestamp.