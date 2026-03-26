from sympy import *
P = Matrix([3,-1])
thita = pi/3
rot = Matrix([[cos(thita),-sin(thita)],[sin(thita),cos(thita)]])
print(rot*P)
refy= Matrix([[-1,0],[0,1]])
print(refy*P)
sc = Matrix([[1/2,0],[0,3]])
print(sc*P)
she = Matrix([[1,-2],[4,1]])
print(she*P)