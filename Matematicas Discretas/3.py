def suma_iterativa(n):
    # calcula S_n = 3 + 3*5 + 3*5^2 + ... + 3*5^n
    total = 0
    for k in range(0, n+1):
        termino = 3 * (5 ** k)

        total = total + termino
    return total

def formula_cerrada(n):
    return 3 * (5 ** (n + 1) - 1) // 4   # // para obtener entero exacto

for n in range(0, 4):
    suma_manual = suma_iterativa(n)
    formula = formula_cerrada(n)
    print(f"n={n}: suma construida = {suma_manual}, fórmula = {formula}, iguales? {suma_manual == formula}")
