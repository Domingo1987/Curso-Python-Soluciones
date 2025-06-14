## Agente de Evaluación - App-api.py

1. **Instala la dependencia** (solo una vez):

    ```bash
    pip install beautifulsoup4
    ```

2. **Asegúrate de tener estos archivos en la carpeta actual:**
    - `App-api.py`
    - `estudiantes.json` (lista de cursos, cada uno con `id` y `slug`)
    - `scrap.txt` (HTML del foro Schoology)

3. **Ejecuta el script así** (cambia por tu archivo y curso):

    ```bash
    python App-api.py <nombre_archivo_salida.json> <id_curso>
    ```

    Ejemplo:
    ```bash
    python App-api.py 3_7_evaluacion.json 1
    ```

El script procesa todo y **guarda el archivo JSON automáticamente** en la carpeta indicada por el `slug` del curso, dentro de `Evaluaciones`.

---

**No necesitas hacer nada más.**

---