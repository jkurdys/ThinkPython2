import turtle
from math import pi

def square(t, l):
    for i in range(4):
        t.fd(l)
        t.lt(90)

def polygon(t, l, n):
    a = 360/n
    polyline(t, n, l, a)
    
def circle(t, r):
    arc(t, r, 360)

def arc(t, r, angle):
    arc_l = (angle/360) * (2 * pi * r)
    n = int(arc_l/3) + 1
    step_l = arc_l / n
    step_angle = angle / n

    polyline(t, n, step_l, step_angle)

def polyline(t, n, l, a):
    for i in range(n):
        t.fd(l)
        t.lt(a)

if __name__ == '__main__':

    bob = turtle.Turtle()
    
    polygon(bob, 100, 5)

    turtle.mainloop()