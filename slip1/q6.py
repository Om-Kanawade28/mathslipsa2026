import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5, 5, 100)
Y = np.linspace(-5,5,100)
X,Y = np.meshgrid(x,Y)
Z=np.sin(X)*np.cos(Y)
fig=plt.figure()
ax = fig.add_subplot(111,projection='3d')
surf = ax.plot_surface(X,Y,Z,cmap='viridis')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Surface Plot')
fig.colorbar(surf)
plt.show()

