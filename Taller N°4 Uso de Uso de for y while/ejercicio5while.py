N = int(input("Ingrese cuántos números triangulares desea ver: "))
print("Los primeros", N, "números triangulares son:")
n = 1
while n <= N:
    triangular = (n * (n + 1)) // 2  # Fórmula del número triangular
    print(triangular)
    n += 1 