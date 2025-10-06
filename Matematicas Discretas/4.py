
def suma_construida(n):
    total = 0
    for k in range(0, n+1):
        termino = 2 * ((-7) ** k)
        total = total + termino
    return total

def formula(n):
    return (1 - (-7) ** (n + 1)) // 4  

for n in range(0, 5):
    s = suma_construida(n)
    f = formula(n)
    print(f"n={n:2d}: suma construida = {s:6d}, formula = {f:6d}, iguales? {s == f}")
