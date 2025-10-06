def suma_cuadrados_impares(n):
    
    suma = 0
    for i in range(n + 1):
        suma += (2*i + 1)**2
    return suma

def formula(n):
    
    return (n + 1)*(2*n + 1)*(2*n + 3) / 3

for n in range(6):
    izquierda = suma_cuadrados_impares(n)
    derecha = formula(n)
    print(f"n = {n} → Izquierda = {izquierda}, Derecha = {derecha}, ¿Iguales?: {izquierda == derecha}")
