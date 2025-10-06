import matplotlib.pyplot as plt

a0 = 5
a1 = -1
a = [a0, a1]

for n in range(2, 10):
    an = a[n-2]
    a.append(an)

print("e) a_n = a_{n-2}")
for i, valor in enumerate(a):
    print(f"a_{i} = {valor}")

plt.plot(range(len(a)), a, marker='D', color='purple', label='a_n = aₙ₋₂')
plt.title("Sucesión e) a_n = a_{n-2}")
plt.xlabel("n")
plt.ylabel("a_n")
plt.grid(True)
plt.legend()
plt.show()
