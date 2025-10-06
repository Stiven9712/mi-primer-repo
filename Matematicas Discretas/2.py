# verifica_suma_pares.py
def suma_pares_iter(n):
    """Suma iterativa de los primeros n pares: 2 + 4 + ... + 2n"""
    s = 0
    for k in range(1, n+1):
        s += 2*k
    return s

def suma_pares_formula(n):
    """Fórmula cerrada: n(n+1)"""
    return n * (n + 1)

# Verificamos de 1 hasta N
def verificar_hasta(N=100):
    todo_bien = True
    for n in range(1, N+1):
        iter_val = suma_pares_iter(n)
        form_val = suma_pares_formula(n)
        if iter_val != form_val:
            print(f"Discrepancia en n={n}: iter={iter_val}, formula={form_val}")
            todo_bien = False
            break
    if todo_bien:
        print(f"Toda la verificación OK para n = 1..{N}")

if __name__ == "__main__":
    verificar_hasta(100)  
