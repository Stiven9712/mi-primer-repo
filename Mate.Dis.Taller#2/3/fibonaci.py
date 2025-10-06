# En este ejemplo se implementa la sucesión de Fibonacci, donde:
# f(0) = 0, f(1) = 1, y f(n) = f(n-1) + f(n-2)

def fibonacci_recursivo(n):
    # f(0) = 0
    if n == 0:
        return 0
    # f(1) = 1
    elif n == 1:
        return 1
    # f(n) = f(n-1) + f(n-2)
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def fibonacci_iterativo(n):
  
    # si n = 0, retorna 0 
    if n == 0:
        return 0

    # inicializamos los dos primeros terminos
    a, b = 0, 1

    # iteramos desde 2 hasta n para construir la secuencia
    for _ in range(2, n + 1):
        a, b = b, a + b  # actualizamos los valores

    # b contiene f(n)
    return b

n = 8

print("recursiva:")
print(f"F({n}) = {fibonacci_recursivo(n)}")

print("iterativa:")
print(f"F({n}) = {fibonacci_iterativo(n)}")
