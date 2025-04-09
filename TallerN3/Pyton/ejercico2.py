# Solicitar al usuario los datos
num1 = float(input("Ingrese el primer número decimal: "))
num2 = float(input("Ingrese el segundo número decimal: "))
operacion = input("Ingrese la operación (+, -, *, /): ")

# Usar match-case para realizar la operación
match operacion:
    case '+':
        resultado = num1 + num2
        print("Resultado:", resultado)
    case '-':
        resultado = num1 - num2
        print("Resultado:", resultado)
    case '*':
        resultado = num1 * num2
        print("Resultado:", resultado)
    case '/':
        if num2 != 0:
            resultado = num1 / num2
            print("Resultado:", resultado)
        else:
            print("Error: División por cero")
    case _:
        print("Operación no válida.")
