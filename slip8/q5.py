import numpy as np
import matplotlib.pyplot as plt

# 3D points
points = np.array([
    [0,0,0],
    [1,0,0],
    [1,1,1]
])

# Plot points
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(points[:,0], points[:,1], points[:,2])

# -------- Rotation about Z-axis --------
theta = np.pi/4   # 45 degree

Rz = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta),  np.cos(theta), 0],
    [0, 0, 1]
])

P = np.array([1,0,0])
P_new = Rz @ P

print("Rotated Point:", P_new)

# Plot rotated point
ax.scatter(P_new[0], P_new[1], P_new[2])

plt.show()