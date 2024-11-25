
import streamlit as st
import openai
from funciones import evaluar_blandas
from funciones import generar_pdf
from funciones import (
    generar_pregunta,
    generar_pregunta_situacional
)

# Inicializar el estado si no existe
if "paso_actual" not in st.session_state:
    st.session_state["paso_actual"] = 1  # Comienza en el Paso 1: Bienvenida
    st.session_state["perfil_seleccionado"] = None
    st.session_state["pregunta_situacional"] = None
    st.session_state["pregunta_tecnica_1"] = None
    st.session_state["pregunta_tecnica_2"] = None
    st.session_state["pregunta_tecnica_3"] = None
    st.session_state["respuesta_situacional"] = None
    st.session_state["respuesta_tecnica_1"] = None
    st.session_state["respuesta_tecnica_2"] = None
    st.session_state["respuesta_tecnica_3"] = None

# Función para avanzar de paso
def avanzar_paso():
    st.session_state["paso_actual"] += 1

# Mostrar el progreso como texto (arriba)
def mostrar_progreso():
    total_pasos = 8
    st.markdown(f"**Paso {st.session_state['paso_actual']} / {total_pasos}**")

# Paso 1: Bienvenida
if st.session_state["paso_actual"] == 1:
    mostrar_progreso()
    st.title("¡Bienvenido al Evaluador Virtual!")
    st.write("""Este cuestionario consta de varios pasos en los que se te harán preguntas situacionales
        y técnicas basadas en tu perfil. Por favor, sigue las instrucciones en cada paso.""")
    st.button("Iniciar", on_click=avanzar_paso, use_container_width=True)

# Paso 2: Selección de Perfil
elif st.session_state["paso_actual"] == 2:
    mostrar_progreso()
    st.title("Evaluador Virtual de Candidatos")
    st.subheader("Seleccione su perfil")
    perfiles = [
        "Seleccione un perfil...",
        "Desarrollador de Software",
        "Consultor de Estrategia",
        "Analista de Marketing",
        "Analista de Logística",
        "Analista Financiero",
    ]
    perfil = st.selectbox("Seleccione el perfil del candidato:", perfiles)

    if perfil != "Seleccione un perfil...":
        st.session_state["perfil_seleccionado"] = perfil
        st.success(f"Perfil seleccionado: {perfil}")
        st.button("Siguiente", on_click=avanzar_paso, use_container_width=True)
    else:
        st.error("⚠️ Por favor, selecciona un perfil para continuar.")

# Paso 3: Pregunta Situacional
elif st.session_state["paso_actual"] == 3:
    mostrar_progreso()
    st.title("Evaluador Virtual de Candidatos")
    st.subheader("Pregunta Situacional")
    perfil = st.session_state.get("perfil_seleccionado", None)

    if perfil:
        # Generar pregunta situacional automáticamente si no existe
        if st.session_state["pregunta_situacional"] is None:
            st.session_state["pregunta_situacional"] = generar_pregunta_situacional(perfil)

        st.write(f"Pregunta situacional: {st.session_state['pregunta_situacional']}")

        # Crear campo de respuesta
        respuesta = st.text_area("Escribe tu respuesta:", value=st.session_state.get("respuesta_situacional", ""))

        # Habilitar o deshabilitar el botón dependiendo si hay contenido en la respuesta
        if respuesta:
            st.session_state["respuesta_situacional"] = respuesta  # Guardar la respuesta
            st.button("Siguiente", on_click=avanzar_paso, use_container_width=True)
        else:
            st.button("Siguiente", disabled=True, use_container_width=True)  # Deshabilitar si no hay respuesta
    else:
        st.error("⚠️ Debes seleccionar un perfil antes de continuar.")

# Paso 4: Primera Pregunta Técnica
elif st.session_state["paso_actual"] == 4:
    mostrar_progreso()
    st.title("Evaluador Virtual de Candidatos")
    st.subheader("Primera Pregunta Técnica")
    perfil = st.session_state.get("perfil_seleccionado", None)

    if perfil:
        # Generar primera pregunta técnica automáticamente si no existe
        if st.session_state["pregunta_tecnica_1"] is None:
            st.session_state["pregunta_tecnica_1"] = generar_pregunta(perfil)

        st.write(f"Primera pregunta técnica: {st.session_state['pregunta_tecnica_1']}")

        # Crear campo de respuesta
        st.session_state["respuesta_tecnica_1"] = "..."
        respuesta = st.text_area("Escribe tu respuesta:", value=st.session_state.get("respuesta_tecnica_1", ""))

        # Habilitar o deshabilitar el botón dependiendo si hay contenido en la respuesta
        if respuesta:
            st.session_state["respuesta_tecnica_1"] = respuesta  # Guardar la respuesta
            st.button("Siguiente", on_click=avanzar_paso, use_container_width=True)
        else:
            st.button("Siguiente", disabled=True, use_container_width=True)  # Deshabilitar si no hay respuesta
    else:
        st.error("⚠️ Debes seleccionar un perfil antes de continuar.")

# Paso 5: Segunda Pregunta Técnica
elif st.session_state["paso_actual"] == 5:
    mostrar_progreso()
    st.title("Evaluador Virtual de Candidatos")
    st.subheader("Segunda Pregunta Técnica")
    perfil = st.session_state.get("perfil_seleccionado", None)

    if perfil:
        # Generar segunda pregunta técnica automáticamente si no existe
        if st.session_state["pregunta_tecnica_2"] is None:
            st.session_state["pregunta_tecnica_2"] = generar_pregunta(perfil)

        st.write(f"Segunda pregunta técnica: {st.session_state['pregunta_tecnica_2']}")

        # Crear campo de respuesta
        st.session_state["respuesta_tecnica_2"] = "...."
        respuesta = st.text_area("Escribe tu respuesta:", value=st.session_state.get("respuesta_tecnica_2", ""))

        # Habilitar o deshabilitar el botón dependiendo si hay contenido en la respuesta
        if respuesta:
            st.session_state["respuesta_tecnica_2"] = respuesta  # Guardar la respuesta
            st.button("Siguiente", on_click=avanzar_paso, use_container_width=True)
        else:
            st.button("Siguiente", disabled=True, use_container_width=True)  # Deshabilitar si no hay respuesta
    else:
        st.error("⚠️ Debes seleccionar un perfil antes de continuar.")

# Paso 6: Tercera Pregunta Técnica
elif st.session_state["paso_actual"] == 6:
    mostrar_progreso()
    st.title("Evaluador Virtual de Candidatos")
    st.subheader("Tercera Pregunta Técnica")
    perfil = st.session_state.get("perfil_seleccionado", None)

    if perfil:
        # Generar tercera pregunta técnica automáticamente si no existe
        if st.session_state["pregunta_tecnica_3"] is None:
            st.session_state["pregunta_tecnica_3"] = generar_pregunta(perfil)

        st.write(f"Tercera pregunta técnica: {st.session_state['pregunta_tecnica_3']}")

        # Crear campo de respuesta
        st.session_state["respuesta_tecnica_3"] = "....."
        respuesta = st.text_area("Escribe tu respuesta:", value=st.session_state.get("respuesta_tecnica_3", ""))

        # Habilitar o deshabilitar el botón dependiendo si hay contenido en la respuesta
        if respuesta:
            st.session_state["respuesta_tecnica_3"] = respuesta  # Guardar la respuesta
            st.button("Mostrar Resultados", on_click=avanzar_paso, use_container_width=True)
        else:
            st.button("Mostrar Resultados", disabled=True, use_container_width=True)  # Deshabilitar si no hay respuesta
    else:
        st.error("⚠️ Debes seleccionar un perfil antes de continuar.")

# Paso 7: Mostrar Evaluaciones
import streamlit as st
from funciones import evaluar_blandas, evaluar_tecnicas

# Este es el paso 7, donde se muestran las evaluaciones
if st.session_state["paso_actual"] == 7:
    # Evaluar habilidades blandas y técnicas
    variables_blandas = ["Empatía", "Colaboración", "Adaptabilidad", "Trabajo en equipo"]
    variables_tecnicas = ["Validez Semántica", "Claridad", "Profundidad Técnica", "Nivel de Dificultad"]

    # Evaluación de las respuestas
    evaluaciones_blandas, justificaciones_blandas = evaluar_blandas(st.session_state["respuesta_situacional"], variables_blandas)
    evaluaciones_tecnicas, justificaciones_tecnicas = evaluar_tecnicas(st.session_state["respuesta_tecnica_1"], variables_tecnicas)

    # Mostrar las evaluaciones de habilidades blandas
    st.write("### Evaluación de Habilidades Blandas")
    for variable in variables_blandas:
        calificacion_blanda = evaluaciones_blandas.get(variable, 'No disponible')
        justificacion_blanda = justificaciones_blandas.get(variable, 'No disponible')
        st.write(f"**{variable}**: ")
        st.write(f"Justificación: {justificacion_blanda}")

    # Mostrar las evaluaciones de habilidades técnicas
    st.write("### Evaluación de Habilidades Técnicas")
    for variable in variables_tecnicas:
        calificacion_tecnica = evaluaciones_tecnicas.get(variable, 'No disponible')
        justificacion_tecnica = justificaciones_tecnicas.get(variable, 'No disponible')
        st.write(f"**{variable}**: ")
        st.write(f"Justificación: {justificacion_tecnica}")

    # Botón para finalizar el cuestionario
    st.button("Finalizar Cuestionario", on_click=avanzar_paso, use_container_width=True)

# Paso 8: Completado y Finalizado
elif st.session_state["paso_actual"] == 8:
    mostrar_progreso()
    st.title("¡Cuestionario Completado!")
    st.write("Gracias por completar el cuestionario. Puedes cerrar esta ventana o reiniciar el formulario.")
