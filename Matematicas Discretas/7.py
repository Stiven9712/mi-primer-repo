def suma_cuadrados(n):
    total = 0
    for i in range(1, n+1):
        total = total + i*i   # i^2
    return total

def formula(n):
    return n*(n+1)*(2*n+1) // 6  # division entera exacta

# Verificar para n=1..10
for n in range(1, 6):
    s = suma_cuadrados(n)
    f = formula(n)
    print(f"n={n:2d} -> suma = {s:3d}, formula = {f:3d}, iguales? {s==f}")
