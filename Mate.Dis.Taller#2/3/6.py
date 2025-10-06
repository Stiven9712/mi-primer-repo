# busqueda binaria, implementación recursiva e iterativa

def busqueda_binaria_recursiva(lista, x, inicio, fin):
    # si el rango es invalido, el elemento no esta en la lista
    if inicio > fin:
        return -1  # -1 indica que no fue encontrado
    
    # calcula el indice del elemento central
    medio = (inicio + fin) // 2

    # si el elemento central es igual a x, quiere decir que se encontro la posicion
    if lista[medio] == x:
        return medio
    
    # si el valor buscado es menor, busca en la mitad izquierda
    elif x < lista[medio]:
        return busqueda_binaria_recursiva(lista, x, inicio, medio - 1)
    
    # si el valor buscado es mayor, busca en la mitad derecha
    else:
        return busqueda_binaria_recursiva(lista, x, medio + 1, fin)

def busqueda_binaria_iterativa(lista, x):
    inicio = 0               # indice inicial
    fin = len(lista) - 1     # indice final

    # mientras el rango sea válido
    while inicio <= fin:
        medio = (inicio + fin) // 2  # calcula el punto medio

        if lista[medio] == x:        # si se encuentra el elemento se retorna su indice
            return medio
        elif x < lista[medio]:       # si el valor buscado es menor, se reduce el rango a la izquierda
            fin = medio - 1
        else:                        # si el valor buscado es mayor, se reduce el rango a la derecha
            inicio = medio + 1

    # si el bucle termina, el elemento no esta en la lista
    return -1

# lista ordenada 
lista = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
x = 12  # valor a buscar

print("recursiva")
resultado_rec = busqueda_binaria_recursiva(lista, x, 0, len(lista) - 1)
print(f"elemento {x} encontrado en la posicion:", resultado_rec)

print("iterativa")
resultado_it = busqueda_binaria_iterativa(lista, x)
print(f"elemento {x} encontrado en la posicion:", resultado_it)