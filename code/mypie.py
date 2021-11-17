import turtle
import math
import numpy as np

def pie(s, l):
    a = 360/s
    for i in range(s):
        t.lt(a)
        tri(l, a/2)

def tri(l, a):
    for i in range(3):
        t.fd(l)
        t.lt(90 + a)
        t.fd()

if __name__ == '__main__':
    t = turtle.Turtle()
    pie(4, 100)
    turtle.mainloop()