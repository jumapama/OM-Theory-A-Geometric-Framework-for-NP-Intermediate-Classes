"""
OM Theory: 3D Visualization of the Foliation Cube and the Intermediate Belt.
Generates the conceptual model showing OM-1, OM-6, and the I-class belt.
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

r = [-1, 1]
X, Y = np.meshgrid(r, r)

# OM-1: NP-Complete (Top Face)
ax.plot_surface(X, Y, np.ones_like(X), color='crimson', alpha=0.7, edgecolor='darkred', lw=2)
ax.text(0, 0, 1.3, "OM-1 (NP-Complete)\nExponential Density", color='darkred', ha='center')

# OM-6: P (Bottom Face)
ax.plot_surface(X, Y, -np.ones_like(X), color='limegreen', alpha=0.7, edgecolor='darkgreen', lw=2)
ax.text(0, 0, -1.4, "OM-6 (Class P)\nPolynomial Density", color='darkgreen', ha='center')

# Intermediate Belt (OM-2..5)
for z_dir in [1, -1]:
    ax.plot_surface(np.ones_like(X)*z_dir, X, Y, color='dodgerblue', alpha=0.3, edgecolor='mediumblue', lw=1)
    ax.plot_surface(X, np.ones_like(X)*z_dir, Y, color='dodgerblue', alpha=0.3, edgecolor='mediumblue', lw=1)

ax.text(1.3, 0, 0, "Intermediate Belt (I)\nInteger Factorization\nDensity $\Theta(n^K \log n)$", color='mediumblue')

# The Caterpillar Heuristic Path
t = np.linspace(0, 2*np.pi, 150)
ax.plot(1.05 * np.cos(t), 1.05 * np.sin(t), 0.5 * np.sin(4*t), color='gold', lw=4, label='Lanczos Search')

ax.set_axis_off()
ax.view_init(elev=20, azim=55)
plt.title("OM Theory: The NP-Intermediate Foliation Cube")
plt.savefig('om_cube_render.png', dpi=300)
print("Render saved as om_cube_render.png")