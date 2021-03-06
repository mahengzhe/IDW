import math
import copy
import matplotlib.pyplot as plt
import numpy as np


def interpolation(lon: np.ndarray, lat: np.ndarray, lst: list) -> np.ndarray :
    a = lon.size
    b = lat.size
    z = np.zeros([a, b])

    for i in range(len(lon)) :
        for j in range(len(lat)) :
            c = lon[i]
            v = lat[j]

            lst1 = selectzone(c, v, lst)  # select the significant zone to reduce computation
            s = 0
            t = 0

            if lst1 != None :
                for k in range(len(lst1)) :

                    d = distance(c, v, lst1[k])  # calculate the distance to all points
                    # calculate as the z={∑[1/(d*d)]*z(i)}/∑[1/(d*d)]
                    if d != 0 :
                        s += (1 / float(d)) * lst1[k][2]  # s=z={∑[1/(d*d)]*z(i)}
                        t += (1 / float(d))  # t=∑[1/(d*d)]
                    else :
                        s = lst1[k][2]
                        t = 1

                z[i][j] = s / t  # z=s/t and load to the 2D array
            else:
                z[i][j]=0
    return z  # get the Z array


def selectzone(lon: float, lat: float, lst: list) -> list :  # determine the zone according to each point
    lst0=copy.copy(lst)
    if lst != None :
        for k in range(len(lst0)) :
            if lon == 0 and lat == 0 :  # at origin point
                return lst0
            elif lon == 0 and lat > 0 :  # at positive y-axis

                if lst0[k][1] < 0 :
                    lst.remove(lst0[k])
                else :
                    if lst0[k][0] != 0 :
                        if lst0[k][1] / lst0[k][0] < 1 or lst0[k][1] / lst0[k][0] > -1 :
                            lst0.remove(lst0[k])

                return lst0

            elif lon == 0 and lat < 0 :  # at negative y-axis

                if lst0[k][1] > 0 :
                    lst0.remove(lst0[k])
                else :
                    if lst0[k][0] != 0 :
                        if lst0[k][1] / lst0[k][0] < 1 or lst0[k][1] / lst0[k][0] > -1 :
                            lst0.remove(lst0[k])

                return lst0
            elif lon > 0 and lat == 0 :  # at positive x-axis

                if lst0[k][0] < 0 :
                    lst0.remove(lst[k])
                else :
                    if lst0[k][0] != 0 :
                        if lst0[k][1] / lst0[k][0] > -1 or lst0[k][1] / lst0[k][0] < 1 :
                            lst0.remove(lst0[k])

                return lst0
            elif lon < 0 and lat == 0 :  # at negative x-axis

                if lst0[k][0] > 0 :
                    lst0.remove(lst0[k])
                else :
                    if lst0[k][0] != 0 :
                        if lst0[k][1] / lst0[k][0] > -1 or lst0[k][1] / lst0[k][0] < 1 :
                            lst0.remove(lst0[k])
                return lst0

            else :  # not at any axis
                if lon > 0 and lat > 0 :  # at the first quadrant
                    if lat / lon > 1 :

                        if lst0[k][0] * lst0[k][1] < 0 or lst0[k][0] < 0 or lst0[k][1] < 0 :
                            lst0.remove(lst0[k])
                        else :
                            if lst0[k][1] / lst0[k][0] < 1 :
                                lst0.remove(lst0[k])

                    else :

                        if lst0[k][0] * lst0[k][1] < 0 or lst0[k][0] or lst0[k][1] < 0 :
                            lst0.remove(lst0[k])
                        else :
                            if lst0[k][1] / lst0[k][0] > 1 :
                                lst0.remove(lst0[k])
                    return lst0
                elif lon < 0 and lat > 0 :  # at the second quadrant
                    if lat / lon > -1 :

                        if lst0[k][0] * lst0[k][1] > 0 or lst0[k][1] < 0 or lst0[k][0] > 0 :
                            lst0.remove(lst0[k])
                        else :
                            if lst0[k][1] / lst0[k][0] < -1 :
                                lst0.remove(lst0[k])
                    else :

                        if lst0[k][0] * lst0[k][1] > 0 or lst0[k][1] < 0 or lst0[k][0] > 0 :
                            lst0.remove(lst0[k])
                        else :
                            if lst0[k][1] / lst0[k][0] > -1 :
                                lst0.remove(lst0[k])
                    return lst
                elif lon < 0 and lat < 0 :  # at the third quadrant
                    if lat / lon > 1 :

                        if lst0[k][0] * lst0[k][1] < 0 or lst0[k][0] > 0 or lst0[k][1] > 0 :
                            lst0.remove(lst0[k])
                        else :
                            if lst0[k][1] / lst0[k][0] < 1 :
                                lst0.remove(lst0[k])
                    else :

                        if lst0[k][1] > 0 or lst0[k][0] > 0 :
                            lst0.remove(lst0[k])
                        else :
                            if lst0[k][1] / lst0[k][0] > 1 :
                                lst0.remove(lst0[k])
                    return lst0
                elif lon > 0 and lat < 0 :  # at the fourth quadrant
                    if lat / lon > -1 :

                        if lst0[k][0] * lst0[k][1] > 0 or lst0[k][1] > 0 or lst0[k][0] < 0 :
                            lst0.remove(lst0[k])
                        else :
                            if lst0[k][1] / lst0[k][0] < -1 :
                                lst0.remove(lst0[k])
                    else :

                        if lst0[k][0] * lst0[k][1] > 0 or lst0[k][1] > 0 or lst0[k][0] < 0 :
                            lst0.remove(lst0[k])
                        else :
                            if lst0[k][1] / lst0[k][0] > -1 :
                                lst0.remove(lst0[k])
                    return lst0
    else :
        return lst

# calculate the disrtance between 2 points
def distance(p1: float, p2: float, pi: float) :
    dis = (p1 - pi[0]) ** 2 + (p2 - pi[1]) ** 2
    m_result = math.sqrt(dis)
    return m_result


if __name__ == '__main__' :
    test = [[1, 1.252, 0.9234], [1.342, 1, 1.1543], [1, 1, 1.0136], [1, 0, 0.9126], [0, 1, 1.1034],
            [1.342, 0.23423, 0.9234], [0.2314, 0.324, 1.0445], [0.342, 0.234, 0.9422], [0.3452, 0.352, 0.956],
            [0.678, 0.735, 0.934],
            [0.534, 0.9843, 1.048], [0.34, 0.98, 1.054]]

    step = 0.01
    x = np.arange(-2, 2, step)
    y = np.arange(-2, 2, step)
    Z = interpolation(x, y, test)

    cs = plt.contourf(x, y, Z)
    # plot the coutour
    plt.colorbar(cs)
    plt.show()
