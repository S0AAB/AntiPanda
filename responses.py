
from dotenv import load_dotenv
from google import genai
import contadorChistes

load_dotenv()
client = genai.Client()

def decidir_accion(mensaje: str) -> str:
    prompt = f"""
    Eres un clasificador.
    Según el mensaje del usuario, responde SOLO con una de estas palabras:
    - "sumar" → Si te piden sumar uno al contador , o que hubo un chiste malo
    - "total" → si el usuario pregunta cuántos chistes malos llevan en la cuenta
    - "reset" → Si el usuario te pide resetear o reiniciar el contador
    - "responder" → si no te piden ninguna de esas tres acciones
    
    Mensaje: "{mensaje}"
    """
    respuesta = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )
    return respuesta.text.strip().lower()

async def manejar_mensaje(mensaje: str) -> str:
    accion = decidir_accion(mensaje)

    print(f"TOMO DECISIÓN: {accion}")

    if accion == "sumar":
        contadorChistes.sumar_chiste_malo()
        return f"Se sumo 1 chiste malo al contador. Lleva {contadorChistes.obtener_total_chistes()}"

    elif accion == "total":
        return f"Panda lleva {contadorChistes.obtener_total_chistes()} chistes malos  "

    elif accion == "reset":
         contadorChistes.reset_contador()
         return f"Se reseteo el contador de los pandichistes"
    elif accion =="responder":
        return responder_mensaje(mensaje)
    else:
        return "No entendí, manito."



def contradecir_mensaje(mensaje: str) -> str:
    prompt = f"Di lo contrario del siguiente mensaje, respuesta corta y concisa: \"{mensaje}\""
    respuesta = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )
    return respuesta.text

def responder_mensaje(mensaje: str) -> str:
    prompt = f"Responde el mensaje siempre con sarcasmo , agresivo y tajante , respuestas cortas: \"{mensaje}\""
    respuesta = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )
    return respuesta.text