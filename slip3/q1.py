#Write a Python program to store a list of 2D points and then sort them in ascending and   
#   descending order of their x-coordinate. 

points = [(3,4),(5,6)]
print(points)
ascending = sorted(points,key=lambda point:point[0])
print(ascending)
des = sorted(points, key=lambda point: point[0],reverse=True)
print(des)    








