# List of points
points = [(3, 2), (1, 5), (4, 1), (2, 3)]

# Ascending order (based on x-coordinate)
asc = sorted(points, key=lambda p: p[0])
print("Ascending:", asc)

# Descending order
desc = sorted(points, key=lambda p: p[0], reverse=True)
print("Descending:", desc)