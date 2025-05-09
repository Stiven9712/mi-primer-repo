#definimos la funcion
def sumar_digitos(numero):
    #validamos que el numero sea entero positivo
    if numero < 0:
        print("por favor, ingrese un numero entero positivo")
        return None 
    #convertimos el numero en cadena para poder recorrer cada digito
    numero_str = str(numero)
    #inicializamos una variable para guardar la suma
    suma = 0
    for digito in numero_str:
        suma +=int(digito)
    return suma
numero_usuario = int(input("ingrese un numero entero positivo: "))
#llamamos a la funcion y mostramos el resultado
resultado = sumar_digitos(numero_usuario)
if resultado is not None:
    print(f"la suma de los digitos de {numero_usuario} es : {resultado}")