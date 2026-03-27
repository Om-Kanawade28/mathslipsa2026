# i) Write a Python program to draw a pentagon. Also find angle at each corner. 
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0,2*np.pi,6)
x = np.cos(theta)
y = np.sin(theta)
plt.plot(x,y)
plt.title("pentagon")
plt.show()
print("angle at each corner:=",(5-2)*180/5)