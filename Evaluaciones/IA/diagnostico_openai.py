import os
from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
assistant_id = os.getenv("OPENAI_ASSISTANT_ID")

if not api_key:
    print("❌ OPENAI_API_KEY no encontrada")
    exit(1)
else:
    print("✅ OPENAI_API_KEY encontrada")

if not assistant_id:
    print("❌ OPENAI_ASSISTANT_ID no encontrada")
    exit(1)
else:
    print("✅ OPENAI_ASSISTANT_ID encontrada")

# Crear cliente
client = OpenAI(api_key=api_key)

print(f"\n🔍 Versión de OpenAI: {OpenAI.__version__ if hasattr(OpenAI, '__version__') else 'Desconocida'}")

# Verificar qué atributos tiene client.beta
print("\n🔍 Atributos disponibles en client.beta:")
beta_attrs = [attr for attr in dir(client.beta) if not attr.startswith('_')]
for attr in beta_attrs:
    print(f"  - {attr}")

# Verificar específicamente si existe responses
if hasattr(client.beta, 'responses'):
    print("✅ client.beta.responses está disponible")
    
    # Verificar métodos de responses
    print("\n🔍 Métodos disponibles en client.beta.responses:")
    response_methods = [attr for attr in dir(client.beta.responses) if not attr.startswith('_')]
    for method in response_methods:
        print(f"  - {method}")
else:
    print("❌ client.beta.responses NO está disponible")

# Verificar si el assistant existe
try:
    assistant = client.beta.assistants.retrieve(assistant_id)
    print(f"✅ Assistant encontrado: {assistant.name}")
    print(f"  - Model: {assistant.model}")
    print(f"  - Instructions: {assistant.instructions[:100]}...")
except Exception as e:
    print(f"❌ Error recuperando assistant: {e}")

print("\n" + "="*50)
print("RESUMEN DEL DIAGNÓSTICO")
print("="*50)