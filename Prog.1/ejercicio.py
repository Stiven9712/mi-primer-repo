def calcular_promedio (lst1):
    suma = 0
    for numero in lst1:
        suma = suma + numero
    promedio = suma / len(lst1)
    return promedio
lista = [8, 3, 3, 5]
print(calcular_promedio(lista))