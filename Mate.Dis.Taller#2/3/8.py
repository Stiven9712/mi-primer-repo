# este algoritmo ordena una lista dividiendola en mitades,
# ordenando recursivamente cada mitad y luego mezclandolas.

# funcion para mezclar dos listas ordenadas 
def mezclar(lista_izq, lista_der):
  
    resultado = []  # lista ordenada
    i = j = 0       # indices para recorrer ambas listas

    # mientras haya elementos en ambas listas
    while i < len(lista_izq) and j < len(lista_der):
        # compara los primeros elementos de cada lista
        if lista_izq[i] <= lista_der[j]:
            resultado.append(lista_izq[i])
            i += 1
        else:
            resultado.append(lista_der[j])
            j += 1

    # agregar los elementos restante
    resultado.extend(lista_izq[i:])
    resultado.extend(lista_der[j:])

    return resultado

def ordenacion_mezcla_recursiva(lista):
   
    # si la lista tiene un solo elemento, ya estq ordenada
    if len(lista) <= 1:
        return lista

    # dividir la lista en dos mitades
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    # ordenar recursivamente ambas mitades
    izquierda_ordenada = ordenacion_mezcla_recursiva(izquierda)
    derecha_ordenada = ordenacion_mezcla_recursiva(derecha)

    # mezclar las dos mitades ordenadas
    return mezclar(izquierda_ordenada, derecha_ordenada)

def ordenacion_mezcla_iterativa(lista):
  
    ancho = 1  # tamaño inicial de las sublistas
    n = len(lista)

    # mientras el tamaño del bloque sea menor que la lista completa
    while ancho < n:
        # tomamos pares de sublistas y las mezclamos
        for i in range(0, n, 2 * ancho):
            izquierda = lista[i:i + ancho]
            derecha = lista[i + ancho:i + 2 * ancho]
            lista[i:i + 2 * ancho] = mezclar(izquierda, derecha)
        # doblamos el tamaño del bloque en cada iteracion
        ancho *= 2

    return lista

lista_original = [8, 2, 4, 6, 9, 7, 10, 1, 5, 3]

print("lista original")
print(lista_original)

ordenada_rec = ordenacion_mezcla_recursiva(lista_original.copy())
print("recursiva")
print(ordenada_rec)

ordenada_it = ordenacion_mezcla_iterativa(lista_original.copy())
print("iterativa")
print(ordenada_it)
