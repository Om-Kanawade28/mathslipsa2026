import numpy as np

# Point P
P = np.array([4, -2])

# a) Reflection in Y-axis
R_y = np.array([
    [-1, 0],
    [ 0, 1]
])
print("Y-axis:", R_y@P)

# b) Scale X by 3
Sx = np.array([
    [3, 0],
    [0, 1]
])
print("Scale X:", Sx @ P)

# c) Scale Y by 2.5
Sy = np.array([
    [1, 0],
    [0, 2.5]
])
print("Scale Y:", Sy @ P)

# d) Reflection in y = -x
Ref = np.array([
    [0, -1],
    [-1, 0]
])
print("y = -x:", Ref @ P)
