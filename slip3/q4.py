from sympy import *
import matplotlib.pyplot as plt

# Square points
points = [Matrix([1,1]), Matrix([3,1]), Matrix([3,3]), Matrix([1,3])]
R=Matrix([[0,-1],[1,0]])
roted = [R*p for p in points]
x = [p[0] for p in points] + [points[0][0]]
y = [p[1] for p in points] + [points[0][1]]
x_r = [p[0] for p in roted] + [roted[0][0]]
y_r = [p[1] for p in roted] + [roted[0][1]]
plt.plot(x,y,'o-',label="orginal")
plt.plot(x_r,y_r,'o-',label="orginal")
plt.legend()
plt.grid()
plt.show()
