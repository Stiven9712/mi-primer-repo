# -----------------------------------------
# EJEMPLO 3: Exponenciación modular
# Verificación entre versión recursiva e iterativa
# -----------------------------------------

# Función recursiva
def expon_mod_recursiva(b, n, m):
    if n == 0:
        return 1
    elif n % 2 == 0:  # si n es par
        mitad = expon_mod_recursiva(b, n // 2, m)
        return (mitad * mitad) % m
    else:  # si n es impar
        return (b * expon_mod_recursiva(b, n - 1, m)) % m


# Función iterativa
def expon_mod_iterativa(b, n, m):
    resultado = 1
    base = b % m
    while n > 0:
        if n % 2 == 1:  # si es impar
            resultado = (resultado * base) % m
        base = (base * base) % m
        n //= 2
    return resultado


# -----------------------------------------
# Comprobación de ambas versiones
# -----------------------------------------

# Datos de prueba
b = 3   # base
n = 13  # exponente
m = 5   # módulo

# Cálculo con ambas funciones
resultado_rec = expon_mod_recursiva(b, n, m)
resultado_it = expon_mod_iterativa(b, n, m)

# Mostrar resultados
print(f"Base = {b}, Exponente = {n}, Módulo = {m}\n")
print(f"Resultado (Recursiva): {resultado_rec}")
print(f"Resultado (Iterativa): {resultado_it}")

# Verificar si coinciden
if resultado_rec == resultado_it:
    print("\n✅ Ambas funciones dan el mismo resultado. La implementación es correcta.")
else:
    print("\n❌ Los resultados no coinciden. Revisa las funciones.")
