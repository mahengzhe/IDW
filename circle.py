#*- coding:UTF-8 -*-
import math

import copy
import matplotlib.pyplot as plt
import numpy as np
import time
import pylab as p
from matplotlib.mlab import griddata

def distance(p1, p2, pi) :
    dis = (p1 - pi[0]) * (p1 - pi[0]) + (p2 - pi[1]) * (p2 - pi[1])
    m_result = math.sqrt(dis)
    return m_result
def distance(p1, p2, pi) :
    dis = (p1 - pi[0]) ** 2 + (p2 - pi[1]) ** 2
    m_result = math.sqrt(dis)
    return m_result


def out_in(lst, x, y, r):
    for n in range(len(lst)) :
        d = distance(x, y, lst[n])
        if d > r :
            return False
        else :
            return True


def circle(lst, r) :
    a = lst[0][0]
    b = lst[0][1]

    theta = np.arange(0, 0.125 * np.pi, 0.01)
    x = a + r * np.cos(theta)
    y = b + r * np.sin(theta)

    fig = plt.figure()
    axes = fig.add_subplot(111)
    axes.plot(x, y)
    plt.show()


def sort(a) :
    b = []
    l = len(a)
    for i in range(l) :
        j = i
        for j in range(l) :
            if (a[i][0] < a[j][0]) :
                a[i], a[j] = a[j], a[i]
            if (a[i][1] > a[j][1]) :
                a[i]= a[j]
                b.append(a[i])
    c = list(set(b))
    c.sort(key=b.index)
    return c
#get the z for the points in the circle and expand from 1/8 circle to the whole circle
def cal_z(c,l):
    X=[]
    Y=[]
    Z=[]

    for n in range(len(c)):
      for m in range(len(l)):
        #get the boundary for each y-axis
        listx = []
        a=c[n][0]
        b=c[n][1]
        x=l[m][0]
        y=l[m][1]
        #calculate the Z value the each point from the center the boundary
        while x<=a:
           s=0
           t=0
           z=0
           x= round(x, 4)

           b=round(b,2)
           d=distance(x,y,c[n])
           d=round(d,4)
           if d != 0 :
              s = s + (1 / (d * d)) * test[m][2]  # s=z={∑[1/(d*d)]*z(i)}
              t = t + (1 / (d * d))  # t=∑[1/(d*d)]
           else :
              s = s + 0
              t = s + 0

           if t != 0 :
              z = s / t  # z=s/t and load to the 2D array
           else :
              z = 0
           z=round(z,4)
           #add the the X,Y,Z as the list from first to fourth quadrant
           listx.append((x, b, z))
           listx.append((-x,b,z))
           listx.append((-x, -b, z))
           listx.append((x, -b, z))
           listx.append((b, x, z))
           listx.append((-b, x, z))
           listx.append((-b, -x, z))
           listx.append ((b, -x, z))
           x=x+0.01
        getX(listx,X)
        getY(listx,Y)
        getZ(listx,Z)

    return X,Y,Z
def getX(l,x):

    for n in range(len(l)):
        x.append(l[n][0])



def getY(l, y)  :
    for n in range(len(l)) :
        y.append(l[n][1])



def getZ(l, z)  :
    for n in range(len(l)) :
        z.append(l[n][2])



if __name__ == '__main__' :

    test = [(1, 1.252, 0.9234), (1.342, 1, 1.1543), (1, 1, 1.0136), (1, 0, 0.9126), (0, 1, 1.1034),(0.678, 0.735, 0.934), (1.342, 0.23423, 0.9234), (0.2314, 0.324, 1.0445), (0.342, 0.234, 0.9422),(0.3452, 0.352, 0.956),(0.534, 0.9843, 1.048), (0.34, 0.98, 1.054)]


    #get the 1/8 circle and find the boundary 
    for n in range(len(test)) :
        s=0
        z=0
        t=0
        a = test[n][0]
        b = test[n][1]
        r = 1
        theta = np.arange(0, 0.25 * np.pi, 0.01)
        x = a + r * np.cos(theta)
        y = b + r * np.sin(theta)
        x = np.around(x, decimals=2)
        y = np.around(y, decimals=2)

        c=[(x[i],y[i]) for i in range(min(len(x),len(y)))]
        z=[]
        c=sort(c)



        X,Y,Z=cal_z(c,test)



    p.scatter(X, Y, color='k')

    # define grid.
    xi = np.linspace(-2, 2, 1000)
    yi = np.linspace(-2, 2, 1000)
    zi = griddata(X, Y, Z, xi, yi,interp='linear')
    cs = p.contour(xi, yi, zi, 10)
    p.clabel(cs, inline=1, fontsize=12)
    p.colorbar()

    p.show()
