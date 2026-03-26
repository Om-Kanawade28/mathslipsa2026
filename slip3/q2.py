from sympy import *
P = Matrix([-2,4])
sh = Matrix([[1,0],[7,1]])
print(sh*P)
sc = Matrix([[7/2,0],[0,7]])
print(sc*P)
shxy=Matrix([[1,4],[7,1]])
print(shxy*P)
thita = pi/3
rot = Matrix([[cos(thita),-sin(thita)],[sin(thita),cos(thita)]])
print(rot*P)