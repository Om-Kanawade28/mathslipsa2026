# ) Write a Python program a point from a list of 2-dimensional points.. Use the min    
#     and max function with a lambda expression as the key. 
# a)   to find leftmost point . b)  to find rightmost point. c) to find topmost point  
# d) to find  bottommost point
# give me simple code to find leftmost, rightmost, topmost and bottommost points from a list of 2-dimensional points using min and max functions with lambda expressions.

points = [(1, 2), (3, 4), (5, 6), (7, 8)]   
leftmost_point = min(points, key=lambda point: point[0])
rightmost_point = max(points, key=lambda point: point[0])       
topmost_point = max(points,key=lambda point:point[1])
bottommost_point = min(points,key=lambda point:point[1])
print("Leftmost point:",leftmost_point)
print("rightmost_point point:",rightmost_point)
print("topmost_point point:",topmost_point)
print("bottommost_point point:",bottommost_point)


