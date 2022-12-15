from turtle import *

t = Turtle()

def fib(n):
    ret = 0
    if (n == 0):
        ret = 1
    else:
        if (n == 1):
            ret = 1
        else:
            ret = fib(n-2) + fib(n-1)
    return ret

def spirale():
    for i in range(20):
        t.circle(i,90)

def spirale_fib(nbr):
    for i in range(nbr):
        t.circle(fib(i),90)

spirale_fib(15)
