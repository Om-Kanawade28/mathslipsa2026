import matplotlib.pyplot as plt

circle = plt.Circle((0, 0), 3, fill=False)

plt.gca().add_patch(circle)
plt.axis('equal')
plt.show()