import matplotlib.pyplot as plt

x = [0,1,1,0,0]
y = [0,0,1,1,0]

# scaled (multiply by 2)
x2 = [i*2 for i in x]
y2 = [i*2 for i in y]

plt.plot(x, y)
plt.plot(x2, y2)

plt.show()