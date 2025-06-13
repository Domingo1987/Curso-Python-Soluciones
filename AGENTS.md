# Agent Instructions

These instructions apply to any file in this repository.

## Evaluation tasks

Only run the evaluation workflow when the user's request explicitly includes the tag `[eval]`.

When asked to evaluate student submissions located in `Evaluaciones/Programacion1_Semi_2025` with names that follow the pattern `3_7_actividad_est.md`, produce a consolidated file named `3_7_actividad.md` in the same folder. Use the following steps:

1. Identify the complete list of students provided in the request or available roster. Ensure that every student appears in the final file, even if they did not submit a solution.
2. For each student file:
   - Extract the student's code and any comments.
   - Evaluate the solution according to the rubric in this file.
3. For students without a submission, create an entry with:
   - **Resolucion:** `no realiza`
   - **Calificacion:** `0/24 [0,0,0,0]`
   - **Comentarios:** `No realiza`
4. Present each student's evaluation using this Markdown structure:

```markdown
### <n>. Nombre: <Nombre Apellido>

**Resolucion:**

```python
<codigo>
```

**Calificacion:** <total>/24 [<c1>, <c2>, <c3>, <c4>]

**Comentarios:**
- <detalle 1>
- <detalle 2>
```

## Rubric
Apply these criteria when assigning the numeric score in **Calificacion**:

1. **Comprension del Problema (0-8 puntos)**
2. **Estructura y Organizacion del Codigo (0-6 puntos)**
3. **Funcionalidad y Exactitud (0-6 puntos)**
4. **Uso de Estrategias y Eficiencia (0-4 puntos)**

The maximum score is 24 points. When reporting a student's grade, show the total followed by the four individual scores in the order above, e.g. `20/24 [7,5,5,3]`.

## Programmatic checks

After modifying repository files, run `python -m py_compile Programas/exportar_calificaciones.py` to ensure scripts compile.
