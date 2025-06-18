from __future__ import annotations

import json
import time
from typing import Any, Dict

from . import data_models
from ..services.openai_service import OpenAIService


openai_service = OpenAIService()
client = openai_service.get_client()


def eval_problema(nombre: str, resolucion: str, rubrica: str) -> Dict[str, Any]:
    """Evalúa una entrega de problema utilizando GPT-4."""
    system_message = (
        "Sos un asistente educativo de evaluación.\n"
        "Vas a recibir un JSON con 'nombre' y 'resolucion'. Evalúa solo si la resolucion contiene una entrega válida. "
        "Si hay enlaces, indica en el comentario si el código fue incluido o solo referenciado.\n\n"
        "RÚBRICA DE EVALUACIÓN:\n"
        f"{rubrica}\n\n"
        "Tu respuesta debe ser SOLO un JSON válido con los campos: 'nombre', 'calificacion' (con 'total' y 'detalle'), y 'comentarios'. "
        "No agregues texto extra antes ni después del JSON."
    )
    input_json = json.dumps({"nombre": nombre, "resolucion": resolucion}, ensure_ascii=False)
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": system_message}, {"role": "user", "content": input_json}],
            temperature=0.0,
            response_format={"type": "json_object"},
            max_tokens=1000,
        )
        return json.loads(response.choices[0].message.content)
    except Exception:
        return {"nombre": nombre, "calificacion": {"total": 0, "detalle": [0, 0, 0, 0]}, "comentarios": "Error en evaluación automática."}


def eval_tarea_response(nombre: str, resolucion: str, tarea: str, assistant_id: str) -> Dict[str, Any]:
    """Evalúa una tarea usando la API de Responses."""
    input_json = {"nombre": nombre, "resolucion": resolucion, "consigna": tarea}
    try:
        response = client.beta.responses.create(
            assistant_id=assistant_id,
            instructions="Evalúa la entrega usando la consigna dada por clave, la rúbrica y la resolución. Devuelve solo el JSON requerido.",
            input=json.dumps(input_json, ensure_ascii=False),
        )
        response_id = response.id
        while True:
            resp_status = client.beta.responses.retrieve(response_id)
            if resp_status.status == "completed":
                break
            elif resp_status.status in ("failed", "cancelled"):
                return {"nombre": nombre, "calificacion": {"total": 0, "detalle": [0, 0, 0, 0]}, "comentarios": "Error en evaluación automática."}
            time.sleep(1)
        final_msg = resp_status.output["content"]
        return json.loads(final_msg)
    except Exception:
        return {"nombre": nombre, "calificacion": {"total": 0, "detalle": [0, 0, 0, 0]}, "comentarios": "Error en evaluación automática."}


def eval_tarea_chat(nombre: str, resolucion: str, tarea: str, system_prompt: str) -> Dict[str, Any]:
    """Evalúa una tarea usando chat completions."""
    input_json = {"nombre": nombre, "resolucion": resolucion, "consigna": tarea}
    user_prompt = (
        "Evalúa la siguiente entrega usando la consigna dada por clave, la rúbrica y la resolución. Devuelve solo el JSON requerido.\n\nDatos de la entrega:\n"
        + json.dumps(input_json, ensure_ascii=False, indent=2)
    )
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}],
            temperature=0,
        )
        final_msg = response.choices[0].message.content.strip()
        if "```json" in final_msg:
            final_msg = final_msg.split("```json")[1].split("```")[0].strip()
        elif "```" in final_msg:
            final_msg = final_msg.split("```")[1].split("```")[0].strip()
        return json.loads(final_msg)
    except Exception:
        return {"nombre": nombre, "calificacion": {"total": 0, "detalle": [0, 0, 0, 0]}, "comentarios": "Error en evaluación automática."}


def eval_tarea_thread(nombre: str, resolucion: str, tarea: str, assistant_id: str) -> Dict[str, Any]:
    """Evalúa una tarea usando threads de OpenAI."""
    input_json = {"nombre": nombre, "resolucion": resolucion, "consigna": tarea}
    try:
        thread = client.beta.threads.create()
        client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=f"Evalúa la siguiente entrega usando la consigna dada por clave, la rúbrica y la resolución. Devuelve solo el JSON requerido.\n\nDatos de la entrega:\n{json.dumps(input_json, ensure_ascii=False, indent=2)}",
        )
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant_id,
            instructions="Evalúa la entrega usando la consigna dada por clave, la rúbrica y la resolución. Devuelve solo el JSON requerido.",
        )
        start_time = time.time()
        while True:
            if time.time() - start_time > 300:
                return {"nombre": nombre, "calificacion": {"total": 0, "detalle": [0, 0, 0, 0]}, "comentarios": "Timeout en evaluación automática."}
            run_status = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
            if run_status.status == "completed":
                break
            elif run_status.status in ("failed", "cancelled", "expired"):
                return {"nombre": nombre, "calificacion": {"total": 0, "detalle": [0, 0, 0, 0]}, "comentarios": f"Error en evaluación automática: {run_status.status}"}
            elif run_status.status == "requires_action":
                time.sleep(2)
            else:
                time.sleep(2)
        messages = client.beta.threads.messages.list(thread_id=thread.id, order="desc")
        assistant_message = next((m for m in messages.data if m.role == "assistant"), None)
        if not assistant_message:
            return {"nombre": nombre, "calificacion": {"total": 0, "detalle": [0, 0, 0, 0]}, "comentarios": "No se recibió respuesta del assistant."}
        final_msg = "".join(c.text.value for c in assistant_message.content if c.type == "text")
        if "```json" in final_msg:
            final_msg = final_msg.split("```json")[1].split("```")[0].strip()
        elif "```" in final_msg:
            final_msg = final_msg.split("```")[1].split("```")[0].strip()
        return json.loads(final_msg)
    except Exception:
        return {"nombre": nombre, "calificacion": {"total": 0, "detalle": [0, 0, 0, 0]}, "comentarios": "Error en evaluación automática."}

