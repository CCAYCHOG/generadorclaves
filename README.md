# Generador de Contraseñas Seguras en Python

Este programa en Python genera contraseñas aleatorias y seguras. Garantiza que cada contraseña contenga al menos una letra mayúscula, una minúscula, un número y un símbolo.

---

## 🛠️ Características

- Contraseñas aleatorias y seguras
- Longitud mínima de 8 caracteres
- Incluye letras, números y símbolos
- Validación de entrada del usuario

---

## 📋 Requisitos

- Python 3.x instalado.

---

## 🚀 Cómo usar

1. Guarda el código en un archivo llamado `generadorclaves.py`.
2. Abre una terminal y ejecuta:

```bash
python generadorclaves.py
```

---

## 💻 Código fuente

```python
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
```

---

## 📌 Autor

**Julio César Caycho García**  
📧 ing@cesarcaycho.com  
📍 Lima, Perú