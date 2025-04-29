#Un número triangular es un número que se puede representar como un triángulo equilátero formado por puntos.
N = int(input("ingrese cuantos numeros triangulares desea ver:"))
print("los primeros", N , "numeros triangulares son:")
for N in range(1,N + 1):
    TRIANGULAR = (N * (N + 1))// 2 
    print(TRIANGULAR)