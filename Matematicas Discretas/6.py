def suma_fracciones_6(n):
    
    suma = 0
    for i in range(1, n + 1):
        suma += 1 / (i * (i + 1))
    return suma

def formula_6(n):
    
    return n / (n + 1)

print("n\tSuma real\tFórmula\t\t¿Iguales?")
print("-" * 45)

for n in range(1, 6):
    suma_real = suma_fracciones_6(n)
    valor_formula = formula_6(n)
    iguales = abs(suma_real - valor_formula) < 1e-10
    print(f"{n}\t{suma_real:.6f}\t{valor_formula:.6f}\t{iguales}")
