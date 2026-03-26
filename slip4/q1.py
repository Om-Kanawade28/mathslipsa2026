import math

# List of 2D points
points = [(3, 4), (1, 1), (0, 2), (5, 5), (2, 0)]

# Sort points based on distance from origin (0,0)
sorted_points = sorted(points, key=lambda point: math.dist(point, (0, 0)))

# Display result
print("Sorted points based on distance from origin:")
for p in sorted_points:
    print(p)