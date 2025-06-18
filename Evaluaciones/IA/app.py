"""Minimal Streamlit app placeholder for step-by-step evaluation."""

import streamlit as st

from patterns import processors
from patterns import evaluators
from services import file_service
from config.settings import load_settings


settings = load_settings()

st.title("Evaluador IA")

step = st.session_state.get("step", 1)

if step == 1:
    st.header("Subir JSON de evaluaciones")
    uploaded = st.file_uploader("Archivo JSON", type="json")
    if uploaded and st.button("Siguiente"):
        data = file_service.read_json(uploaded)
        st.session_state["evaluaciones"] = data
        st.session_state["step"] = 2
        st.experimental_rerun()
elif step == 2:
    st.header("Ejecutar evaluación (mock)")
    data = st.session_state.get("evaluaciones", [])
    if st.button("Evaluar"):
        st.write("Este es un placeholder de evaluación.")
    if st.button("Anterior"):
        st.session_state["step"] = 1
        st.experimental_rerun()
