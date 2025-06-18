import os
import sys
from dotenv import load_dotenv

from patterns.evaluators import eval_tarea_response
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
assistant_id = os.getenv("OPENAI_ASSISTANT_ID")
if not assistant_id:
    raise ValueError("No se encontró OPENAI_ASSISTANT_ID. Agrégalo a .env o usa export.")

if not os.path.exists(archivo_entrada):
    print(f"Error: No se encontró el archivo de entrada: {archivo_entrada}")
    sys.exit(1)

evaluaciones = read_json(archivo_entrada)

for entrega in evaluaciones:
    if entrega.get("resolucion", "").strip().lower() == "no realiza":
        print(f"\n--- {entrega['nombre']} no realiza la entrega, se omite ---")
        continue
    tarea = entrega.get("tarea") or entrega.get("consigna") or "3_7_tarea1"
    resultado = eval_tarea_response(entrega["nombre"], entrega["resolucion"], tarea, assistant_id)
    entrega["calificacion"] = resultado.get("calificacion", {"total": 0, "detalle": [0, 0, 0, 0]})
    entrega["comentarios"] = resultado.get("comentarios", "")

write_json(archivo_salida, evaluaciones)

print(f"\nEvaluación IA terminada. Archivo guardado: {archivo_salida}")
