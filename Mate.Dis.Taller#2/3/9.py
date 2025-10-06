# mezcla de dos listas

def mezcla(L1, L2):
    # L es la lista donde se colocaran los elementos ordenados de L1 y L2
    L = []

    # mientras ambas listas tengan elementos
    while len(L1) > 0 and len(L2) > 0:
        # comparamos los primeros elementos
        if L1[0] < L2[0]:
            # si el de L1 es menor, se añade a L
            L.append(L1.pop(0))
        else:
            # si el de L2 es menor o igual, se añade a L
            L.append(L2.pop(0))

    # cuando una lista se vacia, se añaden los elementos restantes de la otra
    L.extend(L1)
    L.extend(L2)

    # devolvemos la lista ya ordenada
    return L

def ordenacion_mezcla_recursiva(L):
    # si la lista tiene 1 elemento, ya esta ordenada
    if len(L) <= 1:
        return L

    # se divide la lista en dos mitades
    mitad = len(L) // 2
    L1 = L[:mitad]
    L2 = L[mitad:]

    # se ordenan ambas mitades recursivamente
    L1 = ordenacion_mezcla_recursiva(L1)
    L2 = ordenacion_mezcla_recursiva(L2)

    # se mezclan las dos mitades ordenadas
    return mezcla(L1, L2)

def ordenacion_mezcla_iterativa(L):
    # cada elemento de la lista inicial se considera una sublista individual
    sublistas = [[x] for x in L]

    # mientras haya mas de una sublista, se siguen mezclando por pares
    while len(sublistas) > 1:
        nuevas_sublistas = []

        # mezclamos las sublistas de dos en dos
        for i in range(0, len(sublistas), 2):
            # si hay un par de sublistas
            if i + 1 < len(sublistas):
                nueva = mezcla(sublistas[i], sublistas[i + 1])
                nuevas_sublistas.append(nueva)
            else:
                # si queda una sola, se pasa igual
                nuevas_sublistas.append(sublistas[i])

        # reemplazamos las sublistas antiguas por las nuevas
        sublistas = nuevas_sublistas

    # al final solo queda una sublista ordenada
    return sublistas[0]

lista = [8, 2, 4, 6, 9, 7, 10, 1, 5, 3]

print("lista original: ", lista)
print("ordenacion recursiva: ", ordenacion_mezcla_recursiva(lista))
print("ordenacion iterativa: ", ordenacion_mezcla_iterativa(lista))
