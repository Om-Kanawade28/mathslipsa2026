# i) Find the combined transformation of the line segment between the points A [4, −1]   
# and   B[3, 2] by using Python program for the following sequence of transformations:- 
# a) Rotation about origin through an angle   π/4
# 4 
# . 
#      b) Shearing in Y direction by 4 units. 
# c)  Scaling in X− coordinate by 5 units. 
#      d)  
# Reflection through y− axis. 
#simple code
import sympy as sp

# Points (column vectors)
A = sp.Matrix([4, -1])
B = sp.Matrix([3, 2])

# 1. Rotation (π/4)
theta = sp.pi/4
R = sp.Matrix([
    [sp.cos(theta), -sp.sin(theta)],
    [sp.sin(theta),  sp.cos(theta)]
])
print(R*A)
print(R*B)
# 2. Shearing in Y direction (shy = 4)
Sh = sp.Matrix([
    [1, 0],
    [4, 1]
])
print(Sh*A)
print(Sh*B)
# 3. Scaling in X direction (Sx = 5)
Sc = sp.Matrix([
    [5, 0],
    [0, 1]
])
print(Sc*A)
print(Sc*B)
# 4. Reflection about Y-axis
Ref = sp.Matrix([
    [-1, 0],
    [0, 1]
])
print(Ref*A)
print(Ref*B)
# ✅ Combined Transformation Matrix
T = Ref * Sc * Sh * R

print("Combined Transformation Matrix:\n", T)

# Apply transformation
A_new = T * A
B_new = T * B

print("\nTransformed A:", A_new)
print("Transformed B:", B_new)
