N = int(input("¡cuantos numero quieres ingresar?:"))
lista = []
contador = 0 
while contador < N:
    numero = int(input("ingrese un numero:"))
    lista.append(numero)
    contador += 1
print("lista ingresada:", lista)
mayor = lista [0]
indice = 0
while indice < len(lista):
    if lista[indice]> mayor:
        mayor = lista[indice]
    indice += 1
print("el numero mayor es:", mayor )