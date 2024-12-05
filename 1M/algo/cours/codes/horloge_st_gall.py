from turtle import *
from time import *

def carre(t,s):
    s = s/1.3
    for i in range(4):
        t.forward(s)
        t.left(90)

def rond(t,s):
    s = 40/2.5
    t.circle(s)

def croix(t,s):
    t.left(45)
    t.forward(s)
    t.left(180)
    t.forward(s/2)
    t.right(90)
    t.forward(s/2)
    t.left(180)
    t.forward(s)
    t.left(180)
    t.forward(s/2)
    t.left(90)
    t.forward(s/2)
    t.left(135)

def tracer(b,t,s,type):
    pos = t.pos()
    for i in range(len(b)-1,-1,-1):
        print(i,b[i])
        if b[i] == True:
            if type == "h":
                rond(t,s)
            elif type == "m":
                croix(t,s)
            else:
                carre(t,s)
            t.penup()
            t.back(s*2.5)
            t.pendown()
        else:
            t.penup()
            t.back(s*3.5)
            t.pendown()
    t.penup()
    t.goto(pos)
    t.pendown()
            
t = Turtle()
t.pensize(5)
t.pencolor("blue")
t.speed(0)

h = [False, False, False, True, False]
m = [False, False, False, False, True, False]
s = [True, False, False, True, True, True]

size = 40

tracer(h,t,size,"h")
t.penup()
t.right(90)
t.forward(1.5*size)
t.left(90)
t.pendown()
tracer(m,t,size,"m")
t.penup()
t.right(90)
t.forward(1.5*size)
t.left(90)
t.pendown()
tracer(s,t,size,"s")


# croix(t, 40)
# t.penup()
# t.forward(100)
# t.pendown()
# rond(t,40)
# t.penup()
# t.forward(100)
# t.pendown()
# carre(t,40)
#while True:
#    tracer(h)
#    tracer(m)
#    tracer(s)
#    sleep(1)

