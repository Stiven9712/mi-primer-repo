# Solicitar el total de la compra al usuario
total_compra = float(input("Ingrese el total de la compra: "))

# Determinar el costo de envío
if total_compra < 50:
    costo_envio = 10
elif total_compra <= 100:
    costo_envio = 5
else:
    costo_envio = 0

# Mostrar el costo de envío
print("El costo de envío es:", costo_envio)