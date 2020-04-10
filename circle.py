import math

import copy
import matplotlib.pyplot as plt
import numpy as np
import time


def distance(p1: float, p2: float, pi: float) :
    dis = (p1 - pi[0]) ** 2 + (p2 - pi[1]) ** 2
    m_result = math.sqrt(dis)
    return m_result


def out_in(lst: list, x: float, y: float, r=float) -> bool :
    for n in range(len(lst)) :
        d = distance(x, y, lst[n])
        if d > r :
            return False
        else :
            return True


def circle(lst: list, r: float) :
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


if __name__ == '__main__' :

    test = [[1, 1.252, 0.9234], [1.342, 1, 1.1543], [1, 1, 1.0136], [1, 0, 0.9126], [0, 1, 1.1034],
            [0.678, 0.735, 0.934], [1.342, 0.23423, 0.9234], [0.2314, 0.324, 1.0445], [0.342, 0.234, 0.9422],
            [0.3452, 0.352, 0.956],

            [0.534, 0.9843, 1.048], [0.34, 0.98, 1.054]]

    # step = 0.01
    # x = np.arange(-2, 2, step)
    # y = np.arange(-2, 2, step)
    # for i in range(len(x)):
    #      for j in range(len(y)):

    #        print(out_in(test,x[i],y[j],1.23))

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
        print(c)
        for i in range(len(c)):
            a=c[i][0]
            b=c[i][1]
            d=distance(a,b,test[n])
            if d != 0 :
                        s += (1 / float(d)) * test[n][2]  # s=z={∑[1/(d*d)]*z(i)}
                        t += (1 / float(d))  # t=∑[1/(d*d)]
            else :
                        s = test[n][2]
                        t = 1
            
            
            z.append(s/t)
        print(z)

