import matplotlib.pyplot as plt

# Condiciones iniciales
a0 = 2
a1 = 1

# Guardamos los dos primeros términos
a = [a0, a1]

# Generamos los siguientes 10 términos
for n in range(2, 10):
    an = 7*a[n-1] - 10*a[n-2]
    a.append(an)

# Mostrar los resultados
print("b) a_n = 7a_{n-1} - 10a_{n-2}")
for i, valor in enumerate(a):
    print(f"a_{i} = {valor}")

# Graficar la sucesión
plt.plot(range(len(a)), a, marker='o', color='blue', label='a_n = 7aₙ₋₁ - 10aₙ₋₂')
plt.title("Sucesión b) a_n = 7a_{n-1} - 10a_{n-2}")
plt.xlabel("n")
plt.ylabel("a_n")
plt.grid(True)
plt.legend()
plt.show()