# ) Write a Python program using sympy to construct triangles using the following     
# methods.  a) SSS – sides 3, 4, 5. 
# b) ASA – angle = 30°, side = 1, angle = 30° 
# # c) SAS – side = 1, angle = 45°, side = 2. 
#simple code
from sympy import *

A = Point(0,0)
B = Point(3,0)
C = Point(3,4)
t1 = Triangle(A,B,C)
print("sss:",t1)
A = Point(0,0)
B = Point(1,0)
C = Point(1*cos(pi/6),1*sin(pi/6))
# C = Point(1/2,sqrt(3)/2)
t2 = Triangle(A,B,C)
print("asa:",t2)
A = Point(0,0)
B = Point(1,0)
C = Point(1+2*cos(pi/4),2*sin(pi/4))
t3 = Triangle(A,B,C)
print("sas:",t3)

