# i)  Write a Python program to generate a set of points not in general position in   
# 2D space.  
# a) Include at least three collinear points. 
# b) Add some random points that may or may not be collinear. 
# c) Store the points as tuples in a list and print the list. 
import random

# List to store points
points = []

# a) Three collinear points (y = x)
points = [(1,1), (2,2), (3,3)]

# b) Add random points
for i in range(5):
    points.append((random.randint(0,10), random.randint(0,10)))

# c) Print points
print(points)