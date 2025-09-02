
contador_chistes_malos: int = 0

def sumar_chiste_malo() -> None:
    global contador_chistes_malos
    contador_chistes_malos += 1
   

def obtener_total_chistes() -> int:
    return contador_chistes_malos

def reset_contador()->None:
    global contador_chistes_malos
    contador_chistes_malos=0