import matplotlib.pyplot as plt

# Sucesión 1: a_n = 4n - 2
a1 = [2]  
for n in range(2, 21): 
    a1.append(a1[-1] + 4) 

# Sucesión 2: a_n = n(n + 1)
a2 = [2] 
for n in range(2, 21):
    a2.append(a2[-1] + 2 * n)

#Sucesión 3: a_n = n^2
a3 = [1]  
for n in range(2, 21):
    a3.append(a3[-1] + (2 * n - 1))

#Crear lista de índices n
n = list(range(1, 21))

# Mostrar valores por consola 
print("Sucesión 1: a_n = 4n - 2")
print(a1)
print("\nSucesión 2: a_n = n(n + 1)")
print(a2)
print("\nSucesión 3: a_n = n^2")
print(a3)

# Graficar las tres sucesiones
plt.figure(figsize=(8, 5))  
plt.plot(n, a1, marker='o', label='a_n = 4n - 2')
plt.plot(n, a2, marker='s', label='a_n = n(n + 1)')
plt.plot(n, a3, marker='^', label='a_n = n²')

plt.title("Gráficas de las sucesiones recursivas", fontsize=14)
plt.xlabel("n", fontsize=12)
plt.ylabel("a_n", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
