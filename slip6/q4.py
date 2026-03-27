# ii) Write a Python program to plot a saddle surface of the function   𝑧𝑧 = 𝑥𝑥2 − 𝑦𝑦2. /
import numpy as np 
import matplotlib.pyplot as plt
x = np.linspace(-5,5,50)
y = np.linspace(-5,5,50)
X,Y= np.meshgrid(x,y)
Z = X**2 - Y**2
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot_surface(X, Y, Z)
plt.show()
