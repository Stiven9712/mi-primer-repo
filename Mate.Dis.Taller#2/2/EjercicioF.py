import matplotlib.pyplot as plt

a0 = 3
a1 = -3
a = [a0, a1]

for n in range(2, 10):
    an = -6*a[n-1] - 9*a[n-2]
    a.append(an)

print("f) a_n = -6a_{n-1} - 9a_{n-2}")
for i, valor in enumerate(a):
    print(f"a_{i} = {valor}")

plt.plot(range(len(a)), a, marker='p', color='red', label='a_n = -6aₙ₋₁ - 9aₙ₋₂')
plt.title("Sucesión f) a_n = -6a_{n-1} - 9a_{n-2}")
plt.xlabel("n")
plt.ylabel("a_n")
plt.grid(True)
plt.legend()
plt.show()
