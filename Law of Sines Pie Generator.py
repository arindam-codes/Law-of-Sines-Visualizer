from jupyturtle import forward, left, right, penup, pendown
from math import sin, cos, radians

def sin_x(degree):
    degree = radians(degree)
    return sin(degree)


def triangle(theta, length):
    fi = (180 - theta) / 2
    base = ((length * sin_x(theta)) / (sin_x(fi)))
    forward(length)
    left(180 - fi)
    forward(base)
    left(180 - fi)
    forward(length)
    

def draw_pie(n, length):
    theta = 360 / n
    for i in range(n):
        triangle(theta, length)
        left(180)
    
        
        
draw_pie(30, 30)
