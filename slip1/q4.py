#  Write a Python program to apply scaling transformation to a square and plot it.
import numpy as np
import matplotlib.pyplot as plt
sq = np.array([[0,0],[2,0],[2,2],[0,2],[0,0]])
S = np.array([[2,0],[0,3]])
scaled = sq@S
plt.plot(sq[:,0],sq[:,1])
plt.plot(scaled[:,0],scaled[:,1])
plt.gca().set_aspect('equal')
plt.show()
