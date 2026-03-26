import numpy as np
import matplotlib.pyplot as plt

# Parameters
r = 3
h = 5

# Create data
theta = np.linspace(0, 2*np.pi, 50)
z = np.linspace(0, h, 50)
theta, z = np.meshgrid(theta, z)

x = r * np.cos(theta)
y = r * np.sin(theta)

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z)

# Labels
ax.set_title("3D Cylinder")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()