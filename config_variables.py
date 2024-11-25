
# config_variables.py

# Variables y criterios para evaluar habilidades blandas
variables_blandas = {
    "Empatía": {
        "definicion": "Evalúa si el evaluado comprende las emociones o necesidades de otros.",
        "criterios": {
            "10": "Muestra una comprensión excepcional.",
            "7-9": "Buen nivel de empatía, pero sin ejemplos claros.",
            "4-6": "Superficial.",
            "1-3": "Insensible o egoísta."
        },
        "prompt": "Evalúa si esta respuesta muestra empatía hacia los demás. Califica de 1 a 10."
    },
    "Colaboración": {
        "definicion": "Evalúa disposición para trabajar en equipo y valorar perspectivas.",
        "criterios": {
            "10": "Lenguaje proactivo y ejemplos claros.",
            "7-9": "Disposición evidente, pero sin detalles.",
            "4-6": "Vago o secundario.",
            "1-3": "Individualista."
        },
        "prompt": "Evalúa si esta respuesta demuestra disposición para colaborar con otros. Califica de 1 a 10."
    },
    "Adaptabilidad": {
        "definicion": "Evalúa flexibilidad y disposición para ajustarse a cambios.",
        "criterios": {
            "10": "Soluciones claras y flexibles.",
            "7-9": "Disposición a adaptarse, pero con poca evidencia.",
            "4-6": "Superficial o vaga.",
            "1-3": "Resistencia al cambio."
        },
        "prompt": "Evalúa si esta respuesta muestra adaptabilidad a cambios. Califica de 1 a 10."
    },
    "Trabajo en equipo": {
        "definicion": "Evalúa la actitud positiva hacia el trabajo colectivo.",
        "criterios": {
            "10": "Énfasis en el impacto colectivo, con ejemplos.",
            "7-9": "Actitud positiva, pero sin ejemplos específicos.",
            "4-6": "Vago o secundario.",
            "1-3": "Individualista."
        },
        "prompt": "Evalúa si esta respuesta demuestra actitud positiva hacia el trabajo en equipo. Califica de 1 a 10."
    }
}

# Variables y criterios para evaluar habilidades técnicas
variables_tecnicas = {
    "Validez Semántica": {
        "definicion": "Evalúa si la respuesta aborda directamente la pregunta planteada.",
        "criterios": {
            "10": "Respuesta completamente alineada con la pregunta.",
            "7-9": "Alineada pero incompleta.",
            "4-6": "Parcialmente alineada.",
            "1-3": "Irrelevante o incorrecta."
        },
        "prompt": "Evalúa si esta respuesta aborda correctamente la pregunta planteada. Califica de 1 a 10."
    },
    "Claridad": {
        "definicion": "Evalúa qué tan bien estructurada y comprensible es la respuesta.",
        "criterios": {
            "10": "Impecable, sin ambigüedades.",
            "7-9": "Clara, pero con problemas menores.",
            "4-6": "Confusa o desorganizada.",
            "1-3": "Difícil de entender."
        },
        "prompt": "Evalúa la claridad de esta respuesta. Califica de 1 a 10."
    },
    "Profundidad Técnica": {
        "definicion": "Evalúa si la respuesta demuestra conocimiento técnico relevante.",
        "criterios": {
            "10": "Respuesta exhaustiva y detallada.",
            "7-9": "Adecuada pero le faltan algunos detalles.",
            "4-6": "Superficial.",
            "1-3": "Incorrecta o ausente."
        },
        "prompt": "Evalúa la profundidad técnica de esta respuesta. Califica de 1 a 10."
    },
    "Nivel de Dificultad": {
        "definicion": "Clasifica qué tan desafiante es la pregunta para el evaluado.",
        "criterios": {
            "1": "Básica.",
            "2": "Intermedia.",
            "3": "Avanzada."
        },
        "prompt": "Clasifica el nivel de dificultad de esta pregunta como Básica, Intermedia o Avanzada."
    }
}
