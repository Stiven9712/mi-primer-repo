# se muestran dos formas de implementar
# la busqueda lineal de un elemento dentro de una lista
def busqueda_lineal_recursiva(lista, x, i=0):
    
     #Busca un valor x en una lista de manera recursiva
    
      # lista: la lista donde se busca el dato
      # x: el elemento a encontrar
      # i: índice actual, 0 por defecto

    # si recorrio toda la lista y no se encontro x
    if i == len(lista):
        return -1  # retorna -1 si no lo encuentra

    # si el elemento actual es el que se esta buscando
    if lista[i] == x:
        return i  # retorna la posicion donde se encontro

    # avanzar al siguiente indice
    return busqueda_lineal_recursiva(lista, x, i + 1)

def busqueda_lineal_iterativa(lista, x): # busca un valor x en una lista usando un bucle

    # recorre toda la lista elemento por elemento
    for i in range(len(lista)):
        # si el elemento actual es igual a x, se retorna su posicion
        if lista[i] == x:
            return i

    # si el ciclo termina sin encontrar el valor, retorna -1
    return -1

# lista de ejemplo
lista = [4, 7, 1, 9, 12, 3, 5]
x = 12  # elemento a buscar

resultado_rec = busqueda_lineal_recursiva(lista, x)
resultado_it = busqueda_lineal_iterativa(lista, x)

print("recursiva ")
if resultado_rec != -1:
    print(f"el elemento {x} esta en la posicion {resultado_rec}")
else:
    print(f"el elemento {x} no esta en la lista")

print("iterativa ")
if resultado_it != -1:
    print(f"el elemento {x} esta en la posicion {resultado_it}")
else:
    print(f"el elemento {x} no esta en la lista")
