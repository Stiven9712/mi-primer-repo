import matplotlib.pyplot as plt

# Sucesión: a_n = 4n - 2
def a1(n):
    a = [2]  # a1 = 2
    for i in range(2, n + 1):
        a.append(a[-1] + 4)  # a_n = a_(n-1) + 4
    return a

# Parámetros
n = 10
x = list(range(1, n + 1))
y = a1(n)

# Gráfica
plt.plot(x, y, 'o-', color='blue')
plt.title('Sucesión: aₙ = 4n - 2')
plt.xlabel('n')
plt.ylabel('aₙ')
plt.grid(True)
plt.show()
