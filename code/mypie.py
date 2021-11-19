import turtle
import math
import numpy as np

def pie(t, s, l):
    a = 360/s
    for i in range(s):
        tri(t, l, a/2)
        t.lt(a)

def tri(t, l, a):
    y = l * math.sin(a * math.pi / 180)
    
    t.rt(a)
    t.fd(l)
    t.lt(90 + a)
    t.fd(2 * y)
    t.lt(90 + a)
    t.fd(l)
    t.lt(180 - a)

def draw_pies(t, ps, ss, ls):
    t.pu()
    for i in range(ps):
        if i == 0:
            t.fd(-(2*ls[i] + 10))
            t.pd()
            pie(t, ss[i], ls[i])
            t.pu()
        else:
            t.fd(2*ls[i] + 10)
            t.pd()
            pie(t, ss[i], ls[i])
            t.pu()

if __name__ == '__main__':
    t = turtle.Turtle()
    ps = 3
    ss = [5, 6, 7]
    ls = [40, 40, 40]
    draw_pies(t, ps, ss, ls)
    turtle.mainloop()