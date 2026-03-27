# i) Write a Python program to apply each of the following transformations on the point           
# P [−2,4].  
# a) Reflection through the line y = x + 2. 
# b) Scaling in Y -coordinate by factor 2. 
# c) Shearing in X direction by 4 units. 
# d) Rotation about origin by an angle 60 degrees. 
from sympy import *

P = Matrix([-2,4])

# a) Reflection (y = x + 2)
Ref = Matrix([P[1]-2, P[0]+2])
print("Reflection:", Ref)

# b) Scaling (Y by 2)
sc = Matrix([[1,0],[0,2]])
print("Scaling:", sc*P)

# c) Shear in X (4)
she = Matrix([[1,4],[0,1]])
print("Shearing:", she*P)

# d) Rotation (60°)
theta = pi/3
rot = Matrix([[cos(theta),-sin(theta)],
              [sin(theta),cos(theta)]])
print("Rotation:", rot*P)