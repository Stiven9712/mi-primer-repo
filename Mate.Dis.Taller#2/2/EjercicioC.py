import matplotlib.pyplot as plt

a0 = 4
a1 = 10
a = [a0, a1]

for n in range(2, 10):
    an = 6*a[n-1] - 8*a[n-2]
    a.append(an)

print("c) a_n = 6a_{n-1} - 8a_{n-2}")
for i, valor in enumerate(a):
    print(f"a_{i} = {valor}")

plt.plot(range(len(a)), a, marker='s', color='orange', label='a_n = 6aₙ₋₁ - 8aₙ₋₂')
plt.title("Sucesión c) a_n = 6a_{n-1} - 8a_{n-2}")
plt.xlabel("n")
plt.ylabel("a_n")
plt.grid(True)
plt.legend()
plt.show()
