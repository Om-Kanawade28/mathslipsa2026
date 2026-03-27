# ii) Write a Python program to shear a square
from sympy import *
import matplotlib.pyplot as plt
A = Matrix([0,0])
B = Matrix([0,1])
C = Matrix([1,1])
D = Matrix([1,0])
she = Matrix([[1,2],[0,1]])
A1=she*A
B1=she*B
C1=she*C
D1=she*D
x  = [ p[0] for p in[A,B,C,D,A]]
y = [ p[1] for p in [A,B,C,D,A]]
x1  = [ p[0] for p in[A1,B1,C1,D1,A1]]
y1 = [ p[1] for p in [A1,B1,C1,D1,A1]]
plt.plot(x,y,label="original")
plt.plot(x1,y1,label="sheared")
plt.legend()
plt.show()
