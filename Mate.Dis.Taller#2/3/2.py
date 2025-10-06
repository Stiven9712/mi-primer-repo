# algoritmo recursivo para b^n mod m

def exp_mod_recursivo(b, n, m):

    if n == 0:
        return 1

    # verifica si n es par
    if n % 2 == 0:
        # llama recursivamente para calcular la mitad del exponente
        half = exp_mod_recursivo(b, n // 2, m)  
        # eleva al cuadrado y reduce el modulo m
        return (half * half) % m                

    
    else:
         # separa un factor b y reduce n en 1
        return (b * exp_mod_recursivo(b, n - 1, m)) % m
print("recursivo: ", exp_mod_recursivo(3,1,7))

def exp_mod_iterativo(b, n, m):
    # acumula el resultado final
    resultado = 1   
    # reduce la base modulo m para no manejar numeros grandes      
    base = b % m  

    # sigue hasta que n sea a 0
    while n > 0:           
        if n % 2 == 1:     # si n es impar
            resultado = (resultado * base) % m  # multiplicamos resultado por la base
        base = (base * base) % m  # elevamos la base al cuadrado en cada paso
        n //= 2                     # reducimos el exponente dividiendolo entre 2

    return resultado


print("iterativo: ", exp_mod_iterativo(3,1,7))
    
# el ejemplo 3 solo demuestra por inducción matemática que el algoritmo 2 es correcto
# por tanto, se implementa la funcion pow para demostrar que los resultados coinciden 

print(pow(3, 1, 7))
