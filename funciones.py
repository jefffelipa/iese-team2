
import openai
import streamlit as st
import re
from config_variables import variables_blandas, variables_tecnicas
import fpdf
from fpdf import FPDF

from dotenv import load_dotenv
import os
import openai

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# API Key para OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Función para generar pregunta técnica
def generar_pregunta(perfil, respuesta_anterior=None):
    prompt = f"Genera una pregunta técnica robusta y situacional de al menos 5 lineas para un candidato con el perfil de {perfil}."
    if respuesta_anterior:
        prompt += f"\nTen en cuenta esta respuesta previa: {respuesta_anterior}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error al generar la pregunta: {e}"

# Función para generar pregunta situacional
def generar_pregunta_situacional(perfil):
    prompt = (
        f"Basándote en el perfil de {perfil}, genera una pregunta situacional relacionada con trabajo en equipo, colaboración y adaptación al cambio. "
        f"El contexto debe tener al menos 7 líneas de detalle, y la pregunta debe ser breve y clara al final."
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=250
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error al generar la pregunta situacional: {e}"

def evaluar_blandas(respuesta, variables_blandas):
    evaluaciones = {}
    justificaciones = {}

    for variable in variables_blandas:
        # Creamos un prompt sin la pregunta
        prompt = f"Califica la siguiente respuesta sobre '{variable}' del 1 al 10. Respuesta: {respuesta}"

        try:
            # Llamada a OpenAI para obtener la calificación
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=100  # Reducimos los tokens a 200 para asegurar que no se corte
            )

            # Verificamos la respuesta y obtenemos el texto completo
            response_text = response['choices'][0]['message']['content'].strip()

            # Limpiar la justificación (eliminar cualquier texto no deseado, como la pregunta)
            justificacion_limpia = response_text.replace(f"{variable}:", "").strip()

            # Asignamos la calificación a 0 porque no estamos utilizando calificaciones numéricas
            evaluaciones[variable] = 0  # No estamos extrayendo la calificación
            justificaciones[variable] = justificacion_limpia  # Solo la justificación limpia

        except Exception as e:
            st.error(f"Error al llamar a OpenAI: {e}")
            evaluaciones[variable] = 0
            justificaciones[variable] = "No se pudo generar justificación."

    return evaluaciones, justificaciones


def evaluar_tecnicas(respuesta, variables_tecnicas):
    evaluaciones = {}
    justificaciones = {}

    for variable in variables_tecnicas:
        # Simplificamos el prompt
        prompt = f"Califica la siguiente respuesta sobre '{variable}' del 1 al 10. Respuesta: {respuesta}"

        try:
            # Llamada a OpenAI para obtener la calificación
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=100  # Reducimos los tokens a 100
            )

            # Verificamos la respuesta y obtenemos el texto completo
            response_text = response['choices'][0]['message']['content'].strip()

            # Mostramos la respuesta completa como justificación, incluida la calificación
            evaluaciones[variable] = 0  # No estamos extrayendo la calificación
            justificaciones[variable] = response_text  # Mostramos toda la respuesta de OpenAI

        except Exception as e:
            st.error(f"Error al llamar a OpenAI: {e}")
            evaluaciones[variable] = 0
            justificaciones[variable] = "No se pudo generar justificación."

    return evaluaciones, justificaciones

# Función para generar el PDF con las evaluaciones y preguntas
def generar_pdf(perfil, respuesta_situacional, respuesta_tecnica_1, respuesta_tecnica_2, respuesta_tecnica_3):
    # Crear un nuevo documento PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Configurar el título y agregar logo en la parte superior
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, txt="Informe de Evaluación", ln=True, align='C')

    # Agregar logo en la parte superior derecha (Asegúrate de que la ruta del logo sea correcta)
    pdf.image("/content/IESE_LOGO_UPDATED_2023 (1).png", 150, 8, 33)  # Ajusta la ruta del logo según corresponda

    # Margen superior
    pdf.ln(20)

    # Evaluación final del candidato
    evaluacion_blanda, justificaciones_blandas = evaluar_blandas(respuesta_situacional, variables_blandas)
    evaluacion_tecnica, justificaciones_tecnicas = evaluar_tecnicas(respuesta_tecnica_1, variables_tecnicas)

    habilidades_blandas_apto = all([evaluacion >= 7 for evaluacion in evaluacion_blanda.values()])
    habilidades_tecnicas_apto = all([evaluacion >= 7 for evaluacion in evaluacion_tecnica.values()])
    evaluacion_final = "Apto" if habilidades_blandas_apto and habilidades_tecnicas_apto else "No Apto"

    # Agregar evaluación final al PDF
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Evaluación final del candidato: {evaluacion_final}", ln=True)

    # Evaluación de habilidades blandas con justificación dinámica
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Evaluación de habilidades blandas", ln=True)
    pdf.set_font("Arial", size=12)
    for variable, evaluacion in evaluacion_blanda.items():
        pdf.multi_cell(0, 10, txt=f"{variable}: {evaluacion}")
        # Justificación dinámica basada en la calificación
        justificacion = justificaciones_blandas.get(variable, "No disponible")
        pdf.multi_cell(0, 10, txt=f"Justificación: {justificacion}")

    # Evaluación de habilidades técnicas con justificación dinámica
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Evaluación de habilidades técnicas", ln=True)
    pdf.set_font("Arial", size=12)
    for variable, evaluacion in evaluacion_tecnica.items():
        pdf.multi_cell(0, 10, txt=f"{variable}: {evaluacion}")
        # Justificación dinámica basada en la calificación
        justificacion = justificaciones_tecnicas.get(variable, "No disponible")
        pdf.multi_cell(0, 10, txt=f"Justificación: {justificacion}")

    # Recomendación final
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Recomendación final:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt="Basado en la evaluación técnica y blanda, el candidato tiene un buen desempeño general. Se recomienda su contratación, "
                             "aunque sugerimos capacitación en habilidades blandas para mejorar la empatía y creatividad.")

    # Segunda hoja para preguntas y respuestas realizadas
    pdf.add_page()

    # Preguntas y respuestas
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Preguntas y respuestas realizadas", ln=True)
    pdf.set_font("Arial", size=12)

    # Habilidades Blandas
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Preguntas de habilidades blandas", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=f"Pregunta situacional: ¿Cómo manejarías un conflicto en el equipo?\nRespuesta: {respuesta_situacional}")

    # Habilidades Técnicas
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Preguntas de habilidades técnicas", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=f"Pregunta técnica 1: ¿Cómo resolverías un problema complejo de software?\nRespuesta: {respuesta_tecnica_1}")
    pdf.multi_cell(0, 10, txt=f"Pregunta técnica 2: ¿Cómo abordas un análisis de rendimiento en una aplicación?\nRespuesta: {respuesta_tecnica_2}")
    pdf.multi_cell(0, 10, txt=f"Pregunta técnica 3: ¿Cómo manejarías una falla en el sistema de producción?\nRespuesta: {respuesta_tecnica_3}")

    # Salvar el PDF
    pdf_output_path = "/content/Informe_de_evaluacion_candidato.pdf"
    pdf.output(pdf_output_path)

    return pdf_output_path  # Retornar la ruta del archivo generado para su descarga
