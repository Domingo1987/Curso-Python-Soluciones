# 📁 Carpeta: Evaluaciones

Este directorio contiene **todos los recursos y utilidades para la evaluación automatizada** de entregas estudiantiles mediante IA, junto con los datos, resultados y herramientas específicas para cada curso. Está pensado para ser modular, escalable y fácilmente extensible a nuevos cursos, consignas y flujos de evaluación.

---

## 📦 Estructura de carpetas

```
Evaluaciones/
├── IA/
│   ├── app.py                 # App principal (Streamlit) para evaluar entregas y automatizar flujos
│   ├── patterns/
│   │   ├── __init__.py
│   │   ├── processors.py      # Patrones de procesamiento y conversión de datos
│   │   ├── evaluators.py      # Lógica de evaluación automática y uso de IA
│   │   └── data_models.py     # Definición de modelos de datos (dataclasses/Pydantic)
│   ├── services/
│   │   ├── openai_service.py  # Wrapper de OpenAI, GPT, etc.
│   │   ├── file_service.py    # Utilidades de manejo de archivos
│   │   └── export_service.py  # Exportación de resultados
│   ├── utils/
│   │   ├── validators.py      # Validadores de datos y formatos
│   │   └── formatters.py      # Formateo y adaptación de datos
│   ├── config/
│   │   └── settings.py        # Configuraciones generales
│   ├── rubricas.json          # Rúbricas en formato JSON (una o varias, por tarea o curso)
│   ├── estudiantes.json       # Datos estructurados de los estudiantes
│   └── ...otros scripts y recursos generales
│
├── <curso_x>/                 # Carpeta para cada curso (ejemplo: programacion1_semi_2025)
│   ├── consignas.json         # Todas las consignas de este curso
│   ├── entregas/             # Archivos de entregas raw (scrap, txt, csv, html)
│   ├── evaluaciones/         # Resultados de evaluación (JSON, CSV, logs, informes)
│   ├── jsons/                # Datos intermedios (preprocesados, convertidos)
│   ├── ...otros archivos     # Materiales específicos del curso
│
└── README.md                  # (este archivo)
```

---

## 🚦 Flujo de trabajo interactivo (App Evaluadora)

El proceso de evaluación se realiza a través de una app tipo “wizard”, interactiva y paso a paso. **Solo se ve el paso activo en pantalla y el usuario avanza con botones “Anterior/Siguiente”**.

1. **Seleccionar Curso:**

   * El usuario elige un curso. Esto carga automáticamente los estudiantes y consignas del curso.
2. **Seleccionar Consigna:**

   * Se elige la consigna a evaluar (visible y editable si se desea).
3. **Subir o Pegar Scrap:**

   * Se sube el archivo o se pega el HTML del foro/entregas.
4. **Convertir a JSON:**

   * La app convierte los datos a JSON y permite revisarlos/editarlos antes de continuar.
5. **Evaluar con IA:**

   * Se lanza el proceso automático de evaluación/enriquecimiento con IA (OpenAI u otro modelo).
   * Se muestra feedback visual (loader/modal) mientras se procesa.
6. **Ver Resultados:**

   * El usuario visualiza el JSON enriquecido y puede descargarlo/exportarlo.
   * Opcional: ver resumen visual, tabla, badges, etc.

Cada ejecución del flujo **guarda los datos y resultados en la carpeta correspondiente al curso**.

---

## 📄 Gestión de Rúbricas (rubricas.json)

* Todas las rúbricas se definen en un solo archivo JSON (`rubricas.json`), lo que permite gestionar varias rúbricas a la vez, ya sea por tarea, tipo de consigna, curso, etc.
* Cada entrada de rúbrica puede tener:

  * `id` o `nombre`
  * `descripcion`
  * `criterios` (lista con nombre, peso, descripciones y escalas)
* Ventajas: reutilización, edición centralizada, y compatibilidad con la app y los procesos IA.

---

## 🛠️ Ventajas de esta organización

* **Modular y extensible:** fácil agregar nuevos scripts, flujos, evaluadores o servicios IA.
* **Escalable:** cada curso tiene su espacio propio; los datos están separados de la lógica.
* **Visual y usable:** el flujo paso a paso en la app asegura claridad y evita errores.
* **Multi-rúbrica:** soporta múltiples rúbricas por JSON y selección dinámica según la consigna.
* **Preparado para web:** ideal para usar con Streamlit, escalable a la nube sin cambios estructurales.

---

## 📌 Buenas prácticas sugeridas

* Mantener separada la lógica de evaluación de los datos de los cursos.
* Cada curso debe tener su carpeta específica, con sus entregas, consignas y resultados.
* Usar `rubricas.json` para centralizar y versionar criterios de evaluación.
* Documentar los nuevos módulos/scripts agregados dentro de su carpeta respectiva.
* Hacer backups regulares de los resultados y configuraciones.

---

**Cualquier mejora, ajuste o actualización debe documentarse en este README para mantener claridad y coherencia en el proyecto.**
