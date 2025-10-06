def suma_fracciones(n):
    suma = 0
    for i in range(1, n + 1):
        suma += 1 / (2 ** i)
    return suma

def formula(n):
    
    return 1 - (1 / (2 ** n))

# Encabezado de tabla
print("n\tSuma real\tFórmula teórica\t¿Iguales?")
print("-" * 45)

for n in range(1, 5):
    suma_real = suma_fracciones(n)
    valor_formula = formula(n)
    iguales = abs(suma_real - valor_formula) < 1e-10  
    print(f"{n}\t{suma_real:.6f}\t{valor_formula:.6f}\t{iguales}")
