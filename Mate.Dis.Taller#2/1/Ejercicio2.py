import matplotlib.pyplot as plt

# Sucesión: a_n = n(n + 1)
def a2(n):
    a = [2] 
    for i in range(2, n + 1):
        a.append(a[-1] + 2*i) 
    return a

# Parámetros
n = 10
x = list(range(1, n + 1))
y = a2(n)

# Gráfica
plt.plot(x, y, 's-', color='green')
plt.title('Sucesión: aₙ = n(n + 1)')
plt.xlabel('n')
plt.ylabel('aₙ')
plt.grid(True)
plt.show()
