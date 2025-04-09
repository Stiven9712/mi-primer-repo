# Solicitar al usuario el número del mes
mes = int(input("Ingrese el número del mes (1-12): "))

# Usar match-case para determinar la estación del año
match mes:
    case 12 | 1 | 2:
        print("Invierno")
    case 3 | 4 | 5:
        print("Primavera")
    case 6 | 7 | 8:
        print("Verano")
    case 9 | 10 | 11:
        print("Otoño")
    case _:
        print("Mes no válido")