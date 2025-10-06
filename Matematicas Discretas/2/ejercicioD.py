import matplotlib.pyplot as plt

a0 = 4
a1 = 1
a = [a0, a1]

for n in range(2, 10):
    an = 2*a[n-1] - a[n-2]
    a.append(an)

print("d) a_n = 2a_{n-1} - a_{n-2}")
for i, valor in enumerate(a):
    print(f"a_{i} = {valor}")

plt.plot(range(len(a)), a, marker='^', color='green', label='a_n = 2aₙ₋₁ - aₙ₋₂')
plt.title("Sucesión d) a_n = 2a_{n-1} - a_{n-2}")
plt.xlabel("n")
plt.ylabel("a_n")
plt.grid(True)
plt.legend()
plt.show()
