import matplotlib.pyplot as plt
for r in [1,2,3]:
    c = plt.Circle((0,0),r,fill=False)
    plt.gca().add_patch(c)
    
plt.axis('equal')
plt.show()
