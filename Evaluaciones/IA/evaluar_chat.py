import os
import sys
from dotenv import load_dotenv

from patterns.evaluators import eval_tarea_chat
from services.file_service import read_json, write_json

if len(sys.argv) != 3:
    print("Uso: python evaluar_tareas.py archivo_entrada.json archivo_salida.json")
    sys.exit(1)

def ruta_curso(path):
    if os.path.isabs(path):
        return path
    return os.path.join("..", path)

archivo_entrada = ruta_curso(sys.argv[1])
archivo_salida = ruta_curso(sys.argv[2])

# Carga variables de entorno
load_dotenv()

# Verifica que el archivo de entrada exista
if not os.path.exists(archivo_entrada):
    print(f"Error: No se encontró el archivo de entrada: {archivo_entrada}")
    sys.exit(1)

evaluaciones = read_json(archivo_entrada)

SYSTEM_PROMPT = """
Sos un asistente educativo de evaluación.
Tu tarea es analizar entregas de estudiantes de programación.
Antes de evaluar cualquier entrega, debés buscar la consigna original en el archivo de consignas correspondiente (por ejemplo, consignas_p1.json), usando el identificador o nombre de la tarea recibido en el JSON. Utilizá la consigna original como referencia principal para la evaluación.
Si la resolución incluye un enlace a código o notebook, evaluá tanto el texto de la entrega como el contenido de ese enlace (si está presente y es accesible). Si el enlace no se incluye o no es accesible, indicálo en el comentario.

Debes:
- Leer el objeto JSON recibido, que contiene los campos "nombre" (nombre del estudiante), "resolucion" (texto de la entrega), y "consigna" (identificador o nombre de la tarea).
- Buscar la consigna de referencia antes de realizar la evaluación.
- Evaluar la entrega aplicando cuidadosamente la siguiente rúbrica, asegurando que cada criterio esté alineado con lo solicitado en la consigna.

RÚBRICA:
1. Comprensión del Problema (máx. 8 puntos)
2. Estructura y Organización del Código (máx. 6 puntos)
3. Funcionalidad y Exactitud (máx. 6 puntos)
4. Uso de Estrategias y Eficiencia (máx. 4 puntos)

Asigna un puntaje para cada criterio (solo uno por criterio), suma el total y genera un comentario claro y específico para el estudiante, haciendo referencia a la consigna original y la resolución presentada.

Devuelve SIEMPRE el resultado en formato JSON, cumpliendo con el siguiente esquema (no agregues texto antes ni después del JSON):

{
  "nombre": "Nombre del estudiante",
  "calificacion": {
    "total": <suma de los puntajes>,
    "detalle": [<comprension>, <estructura>, <funcionalidad>, <estrategias>]
  },
  "comentarios": "Comentario para el estudiante."
}

Condiciones adicionales:
- Si la consigna no se puede identificar, avisálo en el comentario.
- Si hay enlaces no accesibles, especificálo.
- El comentario debe ser claro, breve y específico sobre la entrega.
"""


# Procesar evaluaciones
print(f"Procesando {len(evaluaciones)} evaluaciones...")

for i, entrega in enumerate(evaluaciones, 1):
    print(f"\n{'='*60}")
    print(f"Procesando {i}/{len(evaluaciones)}: {entrega.get('nombre', 'Sin nombre')}")
    print(f"{'='*60}")

    if entrega.get("resolucion", "").strip().lower() == "no realiza":
        print(f"--- {entrega['nombre']} no realiza la entrega, se omite ---")
        continue

    tarea = entrega.get("tarea") or entrega.get("consigna") or "3_7_tarea1"
    resultado = eval_tarea_chat(entrega["nombre"], entrega["resolucion"], tarea, SYSTEM_PROMPT)

    entrega["calificacion"] = resultado.get("calificacion", {"total": 0, "detalle": [0, 0, 0, 0]})
    entrega["comentarios"] = resultado.get("comentarios", "")

    print(f"✅ Completado: {entrega['nombre']}")

# Guardar resultados
try:
    write_json(archivo_salida, evaluaciones)
    print(f"\n🎉 Evaluación IA terminada. Archivo guardado: {archivo_salida}")
except Exception as e:
    print(f"❌ Error guardando archivo: {e}")
