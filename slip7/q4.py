from sympy import *
from sympy.geometry import *

# -------- Triangle 1 (Isosceles) --------
A = Point(0,0)
B = Point(2,0)
C = Point(1,2)
T1 = Triangle(A,B,C)

print("Triangle 1:", T1)
print("Isosceles:", T1.is_isosceles())
print("Right angled:", T1.is_right())
print("Scalene:", T1.is_scalene())

# -------- Triangle 2 (Right-angled) --------
A = Point(0,0)
B = Point(3,0)
C = Point(0,4)
T2 = Triangle(A,B,C)

print("\nTriangle 2:", T2)
print("Isosceles:", T2.is_isosceles())
print("Right angled:", T2.is_right())
print("Scalene:", T2.is_scalene())

# -------- Triangle 3 (Scalene) --------
A = Point(0,0)
B = Point(4,0)
C = Point(2,3)
T3 = Triangle(A,B,C)

print("\nTriangle 3:", T3)
print("Isosceles:", T3.is_isosceles())
print("Right angled:", T3.is_right())
print("Scalene:", T3.is_scalene())