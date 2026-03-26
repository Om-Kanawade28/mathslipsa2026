# Using sympy declare the points A(0, 2), B(5, 2), C(3, 0) check whether these points are   
# collinear. Declare the line passing through the points A and B, find the distance of this 
# line from point C. 
from sympy import Point,Line
A = Point(0,2)
B = Point(5,2)
C = Point(3,0)
are_collinear = Point.is_collinear(A,B,C)
print("Are ponints collinear:",are_collinear)
line_AB = Line(A,B)
print("equation of line AB:",line_AB)
distance = line_AB.distance(C)
print("Distance from c to line AB:=",distance)

