# Apply following transformation on point P having position vector [2,-5]
#  a) Refection through Y−axis.
#  b) Scaling in X-coordinate by factor 3.
#  c) Shearing in Y-Direction by 3 units.
#  d) Reflection through the line y = − x.
from sympy import Matrix
P = Matrix([2,-5])
R_y = Matrix([[-1,0],
              [0,1]])
print("Reflection Y-axis",R_y*P)
S = Matrix([[3,0],
            [0,1]])
print("Scalling x:",S*P)
Sh_y = Matrix([[1,0],
               [3,1]])
print("Shearing Y:=",Sh_y*P)
R_line = Matrix([[0,-1],
                 [-1,0]])
