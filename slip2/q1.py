points = [(2,3), (4,1), (1,5), (3,2)]

# Minimum y-value point
min_point = min(points, key=lambda p: p[1])

# Maximum y-value point
max_point = max(points, key=lambda p: p[1])

print("Min point:", min_point)
print("Max point:", max_point)
