# Función para verificar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Función que suma los primos en el rango a-b (inclusive)
def suma_primos_en_rango(a, b):
    # Asegurarse de que a sea menor o igual que b
    if a > b:
        a, b = b, a

    suma = 0
    primos_encontrados = []

    for num in range(a, b + 1):
        if es_primo(num):
            primos_encontrados.append(num)
            suma += num

    # Mostrar los primos encontrados
    print(f"Números primos entre {a} y {b}: {primos_encontrados}")

    return suma

# Bloque principal del programa
a = int(input("Ingresa el primer número del rango: "))
b = int(input("Ingresa el segundo número del rango: "))

resultado = suma_primos_en_rango(a, b)
print(f"La suma de los números primos entre {a} y {b} es: {resultado}")