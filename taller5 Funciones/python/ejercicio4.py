# Función para determinar si un año es bisiesto
def es_bisiesto(anio):
    # Paso 1: Verificamos si el año cumple con la condición de bisiesto. Debe ser divisible por 4,No debe ser divisible por 100,También sea divisible por 400.
    if (anio % 4 == 0) and (anio % 100 != 0 or anio % 400 == 0):
        return True
    else:
        return False
# Pedimos al usuario que ingrese un año
anio_usuario = int(input("Ingresa un año: "))

# Llamamos a la función y mostramos el resultado
if es_bisiesto(anio_usuario):
    print(f"El año {anio_usuario} es bisiesto.")
else:
    print(f"El año {anio_usuario} no es bisiesto.")