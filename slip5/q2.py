from sympy import Matrix

# Points
A = Matrix([4, -1])
B = Matrix([3, 0])

# a) Shearing in X (shx = 9)
Sx = Matrix([
    [1, 9],
    [0, 1]
])

# b) Rotation by 180° (π)
R = Matrix([
    [-1, 0],
    [0, -1]
])

# c) Scaling in X by 2
Sc = Matrix([
    [2, 0],
    [0, 1]
])

# d) Reflection about y = x
Ref = Matrix([
    [0, 1],
    [1, 0]
])

# Apply transformations step by step
A_new = Ref * Sc * R * Sx * A
B_new = Ref * Sc * R * Sx * B

print("New A:", A_new)
print("New B:", B_new)