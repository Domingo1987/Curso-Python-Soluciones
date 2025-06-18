import os
import sys
from dotenv import load_dotenv

from patterns.evaluators import eval_tarea_thread
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

# Verifica que el archivo de entrada exista
if not os.path.exists(archivo_entrada):
    print(f"Error: No se encontró el archivo de entrada: {archivo_entrada}")
    sys.exit(1)

evaluaciones = read_json(archivo_entrada)

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
    resultado = eval_tarea_thread(entrega["nombre"], entrega["resolucion"], tarea, assistant_id)
    
    entrega["calificacion"] = resultado.get("calificacion", {"total": 0, "detalle": [0, 0, 0, 0]})
    entrega["comentarios"] = resultado.get("comentarios", "")
    
    print(f"✅ Completado: {entrega['nombre']}")

# Guardar resultados
try:
    write_json(archivo_salida, evaluaciones)
    print(f"\n🎉 Evaluación IA terminada. Archivo guardado: {archivo_salida}")
except Exception as e:
    print(f"❌ Error guardando archivo: {e}")