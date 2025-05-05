
import numpy as np
import matplotlib.pyplot as plt

# Define x values, avoiding 0
x_vals = np.linspace(0.1, 5, 400)

# General solution of the differential equation
def y_func(x, C):
    return x**2 * (C + np.log(x))

# Test with different constants
C_vals = [-2, 0, 2]

plt.figure(figsize=(10, 6))
for C in C_vals:
    y_vals = y_func(x_vals, C)
    plt.plot(x_vals, y_vals, label=f'C = {C}')

plt.title("Solution Curves for $y(x)$ with Different C (Eq: $x y' = x^2 + 2y$)")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
plt.savefig("q1b_plot.png")
from datetime import datetime; print("Run time:", datetime.now())
