# Write a Python program to draw an X–Y axis manually using plotting. Also display a point    
# in specific cordinate
import matplotlib.pyplot as plt
x,y=3,4
plt.axhline(0)   # X-axis
plt.axvline(0)  
plt.plot(x,y,'o')
plt.text(x,y,'(3,4)')
plt.title('X-Y Axis')
# Limits
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid(True)
plt.show()