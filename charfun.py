# charfun.py
# Autor: David AO
# Fecha: Diciembre de 2024
# Descripción: Programa que determina si una cadena es un palíndromo,
#   si no lo es o la entrada no es válida, devuelve False.
import re

def esPalindromo(cadena):
    # Comprueba que la variable es de tipo cadena
    if not isinstance(cadena, str):
        return False
    # Normaliza la cadena para hacer las comparaciones eliminando espacios 
    #   y acentos y signos de puntuación
    cadena = cadena.lower()
    cadena = cadena.replace("á", "a")
    cadena = cadena.replace("é", "e")
    cadena = cadena.replace("í", "i")
    cadena = cadena.replace("ó", "o")
    cadena = cadena.replace("ú", "u")
    cadena = cadena.replace("ü", "u")
    cadena = re.sub(r'[^a-zA-Z0-9ñ]', '', cadena)
    # Comprobar si la cadena es igual a su versión invertida
    return cadena == cadena[::-1]


# Programa principal
if __name__ == "__main__":
    frase = input("Introduzca una frase: ")
    if esPalindromo(frase):
        print("Es un palíndromo!")
    else:
        print("No es un palíndromo!")