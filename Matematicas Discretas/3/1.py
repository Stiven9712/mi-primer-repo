
# Versión recursiva
def suma_pares_recursiva(n):
    if n == 1:
        return 2
    else:
        return suma_pares_recursiva(n - 1) + 2 * n

# Versión directa (fórmula cerrada)
def suma_pares_formula(n):
    return n * (n + 1)

# Mostrar resultados
for n in range(1, 11):
    print(f"n={n}: recursiva = {suma_pares_recursiva(n)}, fórmula = {suma_pares_formula(n)}")
