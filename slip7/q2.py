# ii)  Write a python program to find the combined transformation of the line segment between    
#       the points A[3, 2] & B[2,−3] for the following sequence of transformations:- 
#       a)
#   Rotation about origin through an angle π
# 6
# . 
#       b) Scaling in Y−coordinate by −4 units. 
#       c)
#   Uniform scaling by −6.4 units. 
#      d) Shearing in Y direction by 5 units.

from sympy import *
A = Matrix([3,2])
B = Matrix([2,-3])
t = pi/6
R = Matrix([[cos(t),-sin(t)],[sin(t),cos(t)]])
print("After rotation:-")
print(R*A)
print(R*B)
sc = Matrix([[1,0],[0,-4]])
print("After scaling:")
print(sc*A)
print(sc*B)
usc = Matrix([[-6.4,0],[0,-6.4]])
print("AFter uniform scaling")
print(usc*A)
print(usc*B)
sh = Matrix([[1,0],[5,1]])
print("After shearing:")
print(sh*A)
print(sh*B)
T = sh*usc*sc*R

print("Combined transformation for A:=",T*A)
print("Combined transformation for B:=",T*B)