import json
import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Uso: python evaluar_entregas.py programacion1_semi_2025/3_7_eval.json programacion1_semi_2025/3_7_eval_IA.json

if len(sys.argv) != 3:
    print("Uso: python evaluar_entregas.py archivo_entrada.json archivo_salida.json")
    sys.exit(1)

def ruta_curso(path):
    # Si es absoluta, se deja igual
    if os.path.isabs(path):
        return path
    # Si ejecuta desde Evaluaciones/IA, antepone ../
    return os.path.join("..", path)

archivo_entrada = ruta_curso(sys.argv[1])
archivo_salida = ruta_curso(sys.argv[2])

# Carga la clave automáticamente desde .env si existe
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No se encontró OPENAI_API_KEY. Agrégalo a .env o usa export.")

client = OpenAI(api_key=api_key)

# Lee la rúbrica de problemas (en la misma carpeta que este script)
ruta_script = os.path.dirname(os.path.abspath(__file__))
rubrica_path = os.path.join(ruta_script, "rubrica_problemas.txt")
with open(rubrica_path, "r", encoding="utf-8") as f:
    rubrica = f.read()

# Verifica que el archivo de entrada exista
if not os.path.exists(archivo_entrada):
    print(f"Error: No se encontró el archivo de entrada: {archivo_entrada}")
    sys.exit(1)

# Carga el JSON de evaluaciones desde la ruta indicada
with open(archivo_entrada, "r", encoding="utf-8") as f:
    evaluaciones = json.load(f)

# SYSTEM MESSAGE CON RÚBRICA (y, si lo deseas, letra del problema)
system_message = (
    "Sos un asistente educativo de evaluación.\n"
    "Vas a recibir un JSON con 'nombre' y 'resolucion'. Evalúa solo si la resolución contiene una entrega válida. "
    "Si hay enlaces, indica en el comentario si el código fue incluido o solo referenciado.\n\n"
    "RÚBRICA DE EVALUACIÓN:\n"
    f"{rubrica}\n\n"
    "Tu respuesta debe ser SOLO un JSON válido con los campos: 'nombre', 'calificacion' (con 'total' y 'detalle'), y 'comentarios'. "
    "No agregues texto extra antes ni después del JSON."
)

def evaluar_con_gpt(nombre, resolucion):
    # Arma el JSON de entrada que espera el system
    input_json = json.dumps({"nombre": nombre, "resolucion": resolucion}, ensure_ascii=False)
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # Cambia si lo deseas
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": input_json}
            ],
            temperature=0.0,
            response_format={"type": "json_object"},
            max_tokens=1000
        )
        content = response.choices[0].message.content
        return json.loads(content)
    except Exception as e:
        print(f"[ERROR] Problema evaluando '{nombre}':", e)
        # Devuelve estructura vacía para que el flujo no se interrumpa
        return {
            "nombre": nombre,
            "calificacion": {"total": 0, "detalle": [0, 0, 0, 0]},
            "comentarios": "Error en evaluación automática."
        }

for entrega in evaluaciones:
    if entrega.get("resolucion", "").strip().lower() == "no realiza":
        continue
    resultado = evaluar_con_gpt(entrega["nombre"], entrega["resolucion"])
    entrega["calificacion"] = resultado.get("calificacion", {"total": 0, "detalle": [0, 0, 0, 0]})
    entrega["comentarios"] = resultado.get("comentarios", "")

# Asegura que la carpeta de salida existe
os.makedirs(os.path.dirname(archivo_salida), exist_ok=True)

# Guarda el JSON evaluado
with open(archivo_salida, "w", encoding="utf-8") as f:
    json.dump(evaluaciones, f, ensure_ascii=False, indent=2)

print(f"Evaluación IA terminada. Archivo guardado: {archivo_salida}")
