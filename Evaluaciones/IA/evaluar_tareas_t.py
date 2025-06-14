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

def evaluar_con_assistant(nombre, resolucion, tarea):
    input_json = {
        "nombre": nombre,
        "resolucion": resolucion,
        "consigna": tarea
    }
    print(f"\n--- Enviando evaluación para: {nombre} ---")
    print("JSON enviado a OpenAI:")
    print(json.dumps(input_json, ensure_ascii=False, indent=2))
    
    try:
        # Crear un thread
        thread = client.beta.threads.create()
        print(f"Thread creado: {thread.id}")
        
        # Agregar mensaje al thread
        message_content = f"""Evalúa la siguiente entrega usando la consigna dada por clave, la rúbrica y la resolución. Devuelve solo el JSON requerido.

Datos de la entrega:
{json.dumps(input_json, ensure_ascii=False, indent=2)}"""
        
        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=message_content
        )
        print(f"Mensaje creado: {message.id}")
        
        # Ejecutar el assistant
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant_id,
            instructions="Evalúa la entrega usando la consigna dada por clave, la rúbrica y la resolución. Devuelve solo el JSON requerido."
        )
        print(f"Run creado: {run.id}")
        print(f"Esperando respuesta para {nombre}...")
        
        # Esperar a que termine
        max_wait_time = 300  # 5 minutos máximo
        start_time = time.time()
        
        while True:
            if time.time() - start_time > max_wait_time:
                print(f"[ERROR] Timeout esperando respuesta para {nombre}")
                return {
                    "nombre": nombre,
                    "calificacion": {"total": 0, "detalle": [0, 0, 0, 0]},
                    "comentarios": "Timeout en evaluación automática."
                }
            
            run_status = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
            
            print(f"Status: {run_status.status}")
            
            if run_status.status == "completed":
                break
            elif run_status.status in ("failed", "cancelled", "expired"):
                print(f"[ERROR] Run no completado: {run_status.status}")
                if run_status.last_error:
                    print(f"Error details: {run_status.last_error}")
                return {
                    "nombre": nombre,
                    "calificacion": {"total": 0, "detalle": [0, 0, 0, 0]},
                    "comentarios": f"Error en evaluación automática: {run_status.status}"
                }
            elif run_status.status == "requires_action":
                print(f"[WARNING] Run requiere acción: {run_status.required_action}")
                # Aquí podrías manejar function calls si tu assistant los usa
                time.sleep(2)
            else:
                time.sleep(2)  # Esperar un poco más entre checks
        
        # Obtener mensajes
        messages = client.beta.threads.messages.list(
            thread_id=thread.id,
            order="desc"
        )
        
        # Buscar la respuesta del assistant (primer mensaje con role="assistant")
        assistant_message = None
        for message in messages.data:
            if message.role == "assistant":
                assistant_message = message
                break
        
        if not assistant_message:
            print(f"[ERROR] No se encontró respuesta del assistant para {nombre}")
            return {
                "nombre": nombre,
                "calificacion": {"total": 0, "detalle": [0, 0, 0, 0]},
                "comentarios": "No se recibió respuesta del assistant."
            }
        
        # Extraer el contenido de texto
        final_msg = ""
        for content in assistant_message.content:
            if content.type == "text":
                final_msg += content.text.value
        
        print(f"Respuesta IA para {nombre}:")
        print(final_msg)
        
        # Intentar parsear como JSON
        try:
            # Limpiar la respuesta si viene con markdown
            clean_msg = final_msg
            if "```json" in clean_msg:
                clean_msg = clean_msg.split("```json")[1].split("```")[0].strip()
            elif "```" in clean_msg:
                clean_msg = clean_msg.split("```")[1].split("```")[0].strip()
            
            resultado = json.loads(clean_msg)
            
            # Validar estructura básica
            if "calificacion" not in resultado:
                resultado["calificacion"] = {"total": 0, "detalle": [0, 0, 0, 0]}
            if "comentarios" not in resultado:
                resultado["comentarios"] = "Evaluación completada"
            
            return resultado
            
        except Exception as e:
            print(f"[ERROR] No se pudo parsear respuesta como JSON: {e}")
            print(f"Respuesta recibida: {final_msg}")
            return {
                "nombre": nombre,
                "calificacion": {"total": 0, "detalle": [0, 0, 0, 0]},
                "comentarios": f"Error parseando respuesta: {str(e)}"
            }
        
    except Exception as e:
        print(f"[ERROR] Problema evaluando '{nombre}': {e}")
        import traceback
        traceback.print_exc()
        return {
            "nombre": nombre,
            "calificacion": {"total": 0, "detalle": [0, 0, 0, 0]},
            "comentarios": f"Error en evaluación automática: {str(e)}"
        }

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
    resultado = evaluar_con_assistant(entrega["nombre"], entrega["resolucion"], tarea)
    
    entrega["calificacion"] = resultado.get("calificacion", {"total": 0, "detalle": [0, 0, 0, 0]})
    entrega["comentarios"] = resultado.get("comentarios", "")
    
    print(f"✅ Completado: {entrega['nombre']}")

# Guardar resultados
try:
    os.makedirs(os.path.dirname(archivo_salida), exist_ok=True)
    with open(archivo_salida, "w", encoding="utf-8") as f:
        json.dump(evaluaciones, f, ensure_ascii=False, indent=2)
    print(f"\n🎉 Evaluación IA terminada. Archivo guardado: {archivo_salida}")
except Exception as e:
    print(f"❌ Error guardando archivo: {e}")