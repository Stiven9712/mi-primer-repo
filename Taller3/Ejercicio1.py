# Entrada del usuario
a = float(input("Ingrese la longitud del primer lado: "))
b = float(input("Ingrese la longitud del segundo lado: "))
c = float(input("Ingrese la longitud del tercer lado: "))

# Verificar si los lados forman un triángulo válido
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("El triángulo es: Equilátero")
    elif a == b or a == c or b == c:
        print("El triángulo es: Isósceles")
    else:
        print("El triángulo es: Escaleno")
else:
    print("Los lados ingresados no forman un triángulo válido")
