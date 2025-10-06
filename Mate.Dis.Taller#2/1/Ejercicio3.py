import matplotlib.pyplot as plt

# Sucesión: a_n = n^2
def a3(n):
    a = [1]  # a1 = 1
    for i in range(2, n + 1):
        a.append(a[-1] + (2*i - 1))  # a_n = a_(n-1) + (2n - 1)
    return a

# Parámetros
n = 10
x = list(range(1, n + 1))
y = a3(n)

# Gráfica
plt.plot(x, y, '^-', color='red')
plt.title('Sucesión: aₙ = n²')
plt.xlabel('n')
plt.ylabel('aₙ')
plt.grid(True)
plt.show()
