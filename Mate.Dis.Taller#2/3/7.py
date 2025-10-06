# este ejemplo muestra dos formas de calcular n!

def factorial_recursivo(n):
   
    # si n == 1, el factorial es 1
    if n == 1:
        return 1

    # n! = n * (n - 1)!
    return n * factorial_recursivo(n - 1)

def factorial_iterativo(n):
    
    # inicializamos el resultado en 1
    resultado = 1

    # recorremos desde 1 hasta n, multiplicando en cada paso
    for i in range(1, n + 1):
        resultado *= i

    # resultado contiene n!
    return resultado

n = 6

print("recursiva:")
print(f"{n}! = {factorial_recursivo(n)}")

print("iterativa:")
print(f"{n}! = {factorial_iterativo(n)}")