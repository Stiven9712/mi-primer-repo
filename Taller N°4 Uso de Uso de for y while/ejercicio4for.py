N = int(input("ingrese un numero para calcular su factorial:"))
factorial = 1
for i in range (1, N + 1):
    factorial *= i
print("el factorial del numero ingresado es:", factorial)