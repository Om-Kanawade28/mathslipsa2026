# i) Write a Python program to calculate distance between 3D, using distance formula. What is    
    # typecasting. 
import math 
x1,y1,z1=1,2,3
x2,y2,z2=4,5,6
dist = math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
print("distance:=",dist)
a = 5
b = 2.5
c = a + b   # int → float automatically
print(c)