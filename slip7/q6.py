import numpy as np
import matplotlib.pyplot as plt

# Create data
x = np.linspace(-5, 5, 30)
y = np.linspace(-5, 5, 30)

X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2   # simple surface

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_wireframe(X, Y, Z, color='red')

plt.show()