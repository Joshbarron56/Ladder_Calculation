import math
from visual import *
#Created By Daniel Joshua Barron
#Given the coefficient of Static Friction this code finds the
#minimum angle of that a ladder can have without falling.
#Then it displays a model of that ladder at the minimum angle
scene.height = scene.width = 800


def angl(a):
    ladder.rotate(axis=(0,0,1), angle=(a))

num1 = input("Enter the coefficient of static friction: ")
u = 1/(2*float(num1)) 
result = math.degrees(math.atan(u))
a=(math.atan(u))
print("The ladder can reach a maximum angle of %.2f before slipping" %result)
print("Or %f radians if you're a computer that prefers radians" %a)

        
side = 4.0
thk = 1
s2 = 2*side - thk
s3 = 2*side + thk
floor = box(pos=(0, -side, 0), size=(s3, thk, s3),  color = color.red)
roof = box(pos=(0, side, 0), size=(s3, thk, s3),  color = color.red)
Rwall = box (pos=( side, 0, 0), size=(thk, s2, s3),  color = color.red)
Lwall = box (pos=( -side, 0, 0), size=(thk, s2, s3),  color = color.red)
Bwall = box(pos=(0, 0, -side), size=(s2, s2, thk), color = color.red)
ladder = box(pos=( 2, -1, 0 ), size=(10, .3, 2),  color =color.green)
angl(a)


