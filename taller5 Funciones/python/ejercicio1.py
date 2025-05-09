def es_numero_perfecto(numero):
    #verificar si el numero es menor o igual a 1
    if numero <= 1:
        return False
    #inicializar la suma de los divisores 
    suma_divisores = 0
    #iterar sobre los posibles divisores del numero
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    #verificar si la suma de los divisores es igual al numero
    return suma_divisores == numero 
#solicitar al usuario que ingrese un numero 
numero_ingresado = int (input("ingrese un numero para verificar si es perfecto: "))
#verificar si el numero uingresado es perfecto o no imprimir el resultado
if es_numero_perfecto(numero_ingresado):
    print(f"{numero_ingresado} es un numero perfecto. ")
else:
    print(f"{numero_ingresado} no es un numero perfecto.")