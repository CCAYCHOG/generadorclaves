# Generador de Contraseñas Seguras en Python
import random
import string

def generar_clave(longitud=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation

    clave  = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    clave += random.choices(caracteres, k=longitud - 4)
    random.shuffle(clave)
    return ''.join(clave)

try:
    longitud = int(input("Ingrese la longitud de la clave (mínimo 8): "))
    if longitud < 8:
        raise ValueError("La longitud mínima es 8.")
    clave_generada = generar_clave(longitud)    
    print(f"Clave generada: {clave_generada}")
except ValueError as e:
    print(f"Error: {e}")