import numpy as np
import matplotlib.pyplot as plt
# Interval and segments
def f(t):
    return 200*np.log(140000 / (140000 - 2100*t)) - 9.8*t
# Interval and segments
a = 8
b = 30
n = 6
h = (b-a)/n

# Generate points
t_vals = np.linspace(a, b, n+1)
f_vals = f(t_vals)

# Simpson 3/8 coefficients
I = f_vals[0] + f_vals[-1]  # first + last
for i in range(1, n):
    if i % 3 == 0:
        I += 2 * f_vals[i]
    else:
        I += 3 * f_vals[i]

s = (3*h/8) * I

print(f"Estimated vertical distance s ≈ {s:.4f} meters\n")

# Tabular data
print("{:<5} {:<10} {:<10}".format("i","t_i","f(t_i)"))
for i in range(n+1):
    print("{:<5} {:<10.4f} {:<10.4f}".format(i, t_vals[i], f_vals[i]))

# Plot
t_fine = np.linspace(a, b, 400)
plt.plot(t_fine, f(t_fine), label="f(t)")
plt.scatter(t_vals, f_vals, color='red', label="Evaluation points")
plt.title("Simpson 3/8 Rule Evaluation Points")
plt.xlabel("t (s)")
plt.ylabel("f(t) (m/s)")
plt.grid(True)
plt.legend()
plt.show()
