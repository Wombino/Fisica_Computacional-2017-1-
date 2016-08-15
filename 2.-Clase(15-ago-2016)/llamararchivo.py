from pylab import *


def mi_factorial(n):
    f = 1
    num = range(2, n+1)
    for i in num:
        f = f*i
    return f

def mi_sine(x,n_max):
    x = x%(2*pi)
    y = 0.
    if x<= (pi/2):
        print "intervalo 1"
    elif (pi/2)< x <= pi:
        print "intervalo 2"
        x= pi-x
    elif (pi)< x <= (3*pi/2):
        print "intervalo 3"
        x= pi-x
    else:
        print "intervalo 4"
        x= x-2*pi
    for n in range(n_max):
        p = 2*n + 1
        y = y + ((-1)**n)*(x**(p)/mi_factorial(p))
    return y
