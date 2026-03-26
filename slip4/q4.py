from sympy import Point, Polygon

# Define the vertices
p1 = Point(0, 0)
p2 = Point(1, 0)
p3 = Point(5, 1)
p4 = Point(0, 1)

# Create the polygon
poly = Polygon(p1, p2, p3, p4)

# Check if polygon is convex
is_convex = poly.is_convex()

# Display results
print("Polygon vertices:", poly.vertices)
print("Is the polygon convex?", is_convex)