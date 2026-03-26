from sympy import *
import matplotlib.pyplot  as plt
point = [(3, 3) , (4, 6) , (5, 4) , (4, 2)]
tx,ty=-2,1
x = [p[0] for p in point] + [point[0][0]]
y = [p[1] for p in point]  + [point[0][1]]
txx = [p[0] + tx for p in point] + [point[0][0] + tx]
tyy = [p[1] + ty for p in point]  + [point[0][1] + ty]
plt.plot(x,y,'o-',label="original")
plt.plot(txx,tyy,'o-',label="transform")
plt.legend()
plt.grid()
plt.show()
