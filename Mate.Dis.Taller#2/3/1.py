# calcular la potencia de un numero a^n

# funcion que recibe dos parametros
def potencia_recursiva(a, n):
    # comprueba el paso base si el exponente es 0
    if n == 0:
        return 1
    else:
        # multiplica la base a por el resultado de llamar a la misma funcion pero con un exponente mas pequeño
        return a * potencia_recursiva(a, n - 1)

print("recursivo: ", potencia_recursiva(2, 5)) 



def potencia_iterativa(a, n):

    # inicia el resultado con 1 porque altera la multiplicacion
    resultado = 1     
    # repite el bloque n veces. El _ se usa porque no necesitamos el indice  
    for _ in range(n):     
        resultado *= a     
    return resultado


print("iterativo: ", potencia_iterativa(2, 5))  