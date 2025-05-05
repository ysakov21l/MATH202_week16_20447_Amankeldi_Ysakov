
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from math import comb

def bezier_curve(control_points, n_points=1000):
    n = len(control_points) - 1
    t_vals = np.linspace(0, 1, n_points)
    curve = np.zeros((n_points, 2))
    for i, point in enumerate(control_points):
        bernstein = comb(n, i) * (t_vals ** i) * ((1 - t_vals) ** (n - i))
        curve[:, 0] += bernstein * point[0]
        curve[:, 1] += bernstein * point[1]
    return curve

def plot_bezier(control_pts, order, filename):
    curve = bezier_curve(control_pts)
    cp = np.array(control_pts)
    plt.figure(figsize=(8, 5))
    plt.plot(curve[:, 0], curve[:, 1], label=f'{order} Order Bezier Curve', color='blue')
    plt.plot(cp[:, 0], cp[:, 1], 'ro--', label='Control Points')
    plt.title(f'{order} Order Bezier Curve')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    print(f"{order} order curve saved as {filename}")

control_2nd = [(0, 0), (1, 2), (2, 0)]
control_3rd = [(0, 0), (1, 3), (3, 3), (4, 0)]
control_4th = [(0, 0), (1, 4), (2, 5), (3, 2), (4, 0)]

plot_bezier(control_2nd, "2nd", "bezier_2nd.png")
plot_bezier(control_3rd, "3rd", "bezier_3rd.png")
plot_bezier(control_4th, "4th", "bezier_4th.png")

print("Run time:", datetime.now())
