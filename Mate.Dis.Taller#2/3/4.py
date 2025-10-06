# algoritmos recursivo e iterativo basados en el metodo de euclides y comprobacion del mismo

def mcd_recursivo(a, b):
    # Caso base: si 'a' es 0, el MCD es 'b'
    if a == 0:
        return b
    else:
        # llamada recursiva intercambiando valores:
        # se llama con el residuo de b/a y el valor de a
        # esto reduce el problema hasta que a llegue a 0
        return mcd_recursivo(b % a, a)


def mcd_iterativo(a, b):
    # mientras a no sea 0, se siguen realizando divisiones sucesivas
    while a != 0:
        # Se reemplaza a por el residuo y b por el valor anterior de a
        a, b = b % a, a
    # cuando a es 0, retorna el valor de b
    return b


print("recursivo:", mcd_recursivo(27, 36))
print("iterativo:", mcd_iterativo(27, 36))

# Comprobación con la función incorporada de Python

