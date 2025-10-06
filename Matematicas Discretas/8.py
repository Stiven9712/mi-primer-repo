def suma_cubos(n):
    total = 0
    for i in range(1, n+1):
        total = total + i**3
    return total

def formula(n):
    return (n*(n+1)//2) ** 2  # uso // para mantener entero

for n in range(1, 6):
    s = suma_cubos(n)
    f = formula(n)
    print(f"n={n:2d} -> suma = {s:6d}, formula = {f:6d}, iguales? {s==f}")
