# Función para verificar si una cadena es un palíndromo
def es_palindromo(texto):
    # Paso 1: Convertimos todo el texto a minúsculas
    texto = texto.lower()

    # Paso 2: Quitamos los espacios en blanco
    texto = texto.replace(" ", "")

    # Paso 3: Comparamos el texto con su reverso
    return texto == texto[::-1]

# Bloque principal del programa
# Pedimos al usuario que ingrese una frase
cadena = input("Ingresa una frase o palabra: ")

# Llamamos a la función y mostramos el resultado
if es_palindromo(cadena):
    print(f'"{cadena}" es un palíndromo.')
else:
    print(f'"{cadena}" no es un palíndromo.')