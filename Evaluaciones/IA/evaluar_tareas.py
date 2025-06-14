import json
import os
import sys
import time
from openai import OpenAI
from dotenv import load_dotenv

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
api_key = os.getenv("OPENAI_API_KEY")
assistant_id = os.getenv("OPENAI_ASSISTANT_ID")
if not api_key:
    raise ValueError("No se encontró OPENAI_API_KEY. Agrégalo a .env o usa export.")
if not assistant_id:
    raise ValueError("No se encontró OPENAI_ASSISTANT_ID. Agrégalo a .env o usa export.")

# Instancia del cliente
client = OpenAI(api_key=api_key)

# Verifica que el archivo de entrada exista
if not os.path.exists(archivo_entrada):
    print(f"Error: No se encontró el archivo de entrada: {archivo_entrada}")
    sys.exit(1)

# Carga el JSON de evaluaciones desde la ruta indicada
with open(archivo_entrada, "r", encoding="utf-8") as f:
    evaluaciones = json.load(f)

def evaluar_con_assistant_responses(nombre, resolucion, tarea):
    input_json = {
        "nombre": nombre,
        "resolucion": resolucion,
        "consigna": tarea
    }
    print(f"\n--- Enviando evaluación para: {nombre} ---")
    print("JSON enviado a OpenAI:")
    print(json.dumps(input_json, ensure_ascii=False, indent=2))
    try:
        # Intentar usar la nueva Responses API (debe tener openai >= 1.13.3)
        response = client.beta.responses.create(
            assistant_id=assistant_id,
            instructions="Evalúa la entrega usando la consigna dada por clave, la rúbrica y la resolución. Devuelve solo el JSON requerido.",
            input=json.dumps(input_json, ensure_ascii=False)
        )

        response_id = response.id
        print(f"Esperando respuesta para {nombre}... (response_id: {response_id})")
        while True:
            resp_status = client.beta.responses.retrieve(response_id)
            if resp_status.status == "completed":
                break
            elif resp_status.status in ("failed", "cancelled"):
                print(f"[ERROR] Assistant Response no completado: {resp_status.status}")
                return {
                    "nombre": nombre,
                    "calificacion": {"total": 0, "detalle": [0, 0, 0, 0]},
                    "comentarios": "Error en evaluación automática."
                }
            time.sleep(1)

        # Respuesta final
        final_msg = resp_status.output["content"]
        print(f"Respuesta IA para {nombre}:")
        print(final_msg)
        try:
            return json.loads(final_msg)
        except Exception as e:
            print(f"[ERROR] Respuesta no válida: {e}\n{final_msg}")
            return {
                "nombre": nombre,
                "calificacion": {"total": 0, "detalle": [0, 0, 0, 0]},
                "comentarios": "Error en evaluación automática."
            }

    except Exception as e:
        print(f"[ERROR] Problema evaluando '{nombre}': {e}")
        return {
            "nombre": nombre,
            "calificacion": {"total": 0, "detalle": [0, 0, 0, 0]},
            "comentarios": "Error en evaluación automática."
        }

for entrega in evaluaciones:
    if entrega.get("resolucion", "").strip().lower() == "no realiza":
        print(f"\n--- {entrega['nombre']} no realiza la entrega, se omite ---")
        continue
    tarea = entrega.get("tarea") or entrega.get("consigna") or "3_7_tarea1"
    resultado = evaluar_con_assistant_responses(entrega["nombre"], entrega["resolucion"], tarea)
    entrega["calificacion"] = resultado.get("calificacion", {"total": 0, "detalle": [0, 0, 0, 0]})
    entrega["comentarios"] = resultado.get("comentarios", "")

os.makedirs(os.path.dirname(archivo_salida), exist_ok=True)

with open(archivo_salida, "w", encoding="utf-8") as f:
    json.dump(evaluaciones, f, ensure_ascii=False, indent=2)

print(f"\nEvaluación IA terminada. Archivo guardado: {archivo_salida}")
