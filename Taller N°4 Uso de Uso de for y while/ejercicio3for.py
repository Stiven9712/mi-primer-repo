N = int(input("¿Cuántos números quieres ingresar?: "))

# Crear la lista vacía
lista = []
for _ in range(N):
    numero = int(input("Ingresa un número: "))
    lista.append(numero)
print("Lista ingresada:", lista)
mayor = lista[0]  
for num in lista:
    if num > mayor:
        mayor = num
print("el numero mayor es:", mayor)