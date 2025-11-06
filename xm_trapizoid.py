import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import isfinite

# Differential integrand
def f(t):
    return 200*np.log(140000 / (140000 - 2100*t)) - 9.8*t

# Interval
a = 8.0
b = 30.0

# (i) Single-segment trapezoidal rule
fa = f(a)
fb = f(b)
I_trap = (b - a) / 2 * (fa + fb)

# (ii) "True" value using a very fine composite Simpson rule
# Use large even n for high accuracy
n = 12000
if n % 2 == 1:
    n += 1
x = np.linspace(a, b, n+1)
y = f(x)

h = (b - a) / n
# Composite Simpson's rule
I_simpson = (h/3) * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2]))

# (ii) True error
E_t = I_simpson - I_trap

# (iii) Absolute relative true error (percentage)
abs_rel_true_error = abs(E_t) / abs(I_simpson) * 100 if isfinite(I_simpson) and I_simpson != 0 else np.nan

# Prepare tabular data (endpoints and some sample points)
t_points = np.array([a, (a+b)/2, b])
f_points = f(t_points)
# For trapezoid, contribution of each endpoint to trapezoid area:
contrib = (b-a)/2 * f_points
table = pd.DataFrame({
    "t (s)": t_points,
    "f(t)": f_points,
    "Trapezoid contribution": contrib
})

# Print numeric results and show table & plot
print("Single-segment Trapezoidal approximation (i):")
print(f"I_trap = {I_trap:.8f} meters\n")

print("(ii) 'True' value approximated by composite Simpson (n = {:d}):".format(n))
print(f"I_simpson ≈ {I_simpson:.12f} meters\n")

print("(iii) True error and absolute relative true error:")
print(f"E_t = I_simpson - I_trap = {E_t:.12f} meters")
print(f"Absolute relative true error = {abs_rel_true_error:.6f} %\n")

# Display table to user
import caas_jupyter_tools as tools
tools.display_dataframe_to_user("Function values and trapezoid contributions", table)

# Plot the integrand and mark endpoints
t_fine = np.linspace(a, b, 800)
y_fine = f(t_fine)

plt.figure(figsize=(9,5))
plt.plot(t_fine, y_fine, label="f(t)")
plt.scatter(t_points, f_points)  # endpoints and midpoint
# Shade trapezoid area (single trapezoid between a and b)
plt.fill_between([a, b], [fa, fb], alpha=0.25)
plt.title("Integrand f(t) and single-segment trapezoid on [8,30]")
plt.xlabel("t (s)")
plt.ylabel("f(t)")
plt.legend()
plt.grid(True)
plt.show()

