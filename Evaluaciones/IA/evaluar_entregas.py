import os
import sys

from dotenv import load_dotenv

from patterns.evaluators import eval_problema
from services.file_service import read_json, write_json

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

# Lee la rúbrica de problemas (en la misma carpeta que este script)
ruta_script = os.path.dirname(os.path.abspath(__file__))
rubrica_path = os.path.join(ruta_script, "rubrica_problemas.txt")
with open(rubrica_path, "r", encoding="utf-8") as f:
    rubrica = f.read()

# Verifica que el archivo de entrada exista
if not os.path.exists(archivo_entrada):
    print(f"Error: No se encontró el archivo de entrada: {archivo_entrada}")
    sys.exit(1)

evaluaciones = read_json(archivo_entrada)

for entrega in evaluaciones:
    if entrega.get("resolucion", "").strip().lower() == "no realiza":
        continue
    resultado = eval_problema(entrega["nombre"], entrega["resolucion"], rubrica)
    entrega["calificacion"] = resultado.get("calificacion", {"total": 0, "detalle": [0, 0, 0, 0]})
    entrega["comentarios"] = resultado.get("comentarios", "")


write_json(archivo_salida, evaluaciones)

print(f"Evaluación IA terminada. Archivo guardado: {archivo_salida}")
