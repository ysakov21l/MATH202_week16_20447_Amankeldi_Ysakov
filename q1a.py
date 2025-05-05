
import numpy as np
import matplotlib.pyplot as plt

x_vals = np.linspace(0.1, 5, 400)

def y_func(x, C):
    return (C / x**2) + (np.exp(x) * (1 - 1/x)) / x

C_vals = [-5, 0, 5]

plt.figure(figsize=(10, 6))
for C in C_vals:
    y_vals = y_func(x_vals, C)
    plt.plot(x_vals, y_vals, label=f'C = {C}')

plt.title("Solution Curves for $y(x)$ with Different C (Eq: $x y' + 2y = e^x$)")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
plt.savefig("q1a_plot.png")
print("Plot saved as q1a_plot.png")
import datetime; print("Run time:", datetime.datetime.now())
