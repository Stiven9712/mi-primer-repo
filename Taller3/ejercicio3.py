# Solicitar la calificación numérica al usuario
calificacion = float(input("Ingrese la calificación numérica: "))

# Determinar la calificación en letra
if 90 <= calificacion <= 100:
    letra = "A"
elif 80 <= calificacion < 90:
    letra = "B"
elif 70 <= calificacion < 80:
    letra = "C"
elif 60 <= calificacion < 70:
    letra = "D"
else:
    letra = "F"

# Mostrar la calificación en letra
print("La calificación en letra es:", letra)