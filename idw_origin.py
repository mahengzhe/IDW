import math
import matplotlib.pyplot as plt
import numpy as np

def interpolation(lon:list,lat:list,lst:list)-> list :


    d=0
    s=0
    t=0

    a=lon.size
    b=lat.size
    z= np.zeros([a, b])
    for i in range(len(lon)):
        for j in range(len(lat)):
            for k in range(len(lst)):
                d=distance(lon[i],lat[j],lst[k])#calculate the distance to all points
                #calculate as the z={∑[1/(d*d)]*z(i)}/∑[1/(d*d)]
                if d!=0:
                    s=s+(1/(d*d))*lst[k][2] # s=z={∑[1/(d*d)]*z(i)}
                    t=t+(1/(d*d))           # t=∑[1/(d*d)]
                else :
                    s=s+0
                    t=s+0
                k = k + 1
            if t!=0:
              z[i][j]=s/t                   #z=s/t and load to the 2D array
            else:
                z[i][j]=0
            j=j+1
        i=i+1
    return z                                #get the Z array
# calculate the disrtance between 2 points
def distance(p1:float,p2:float, pi:float) :
    dis = (p1 - pi[0]) * (p1 - pi[0]) + (p2 - pi[1]) * (p2 - pi[1])
    m_result = math.sqrt(dis)
    return m_result

#main

test=[[1,1.252,0.9234],[1.342,1,1.1543],[1,1,1.0136],[1,0,0.9126],[0,1,1.1034],[1.342,0.23423,0.9234],[0.2314,0.324,1.0445],[0.342,0.234,0.9422],[0.3452,0.352,0.956],[0.678,0.735,0.934],
      [0.534,0.9843,1.048],[0.34,0.98,1.054]]



step = 0.01
x = np.arange(-2,2,step)
y = np.arange(-2,2,step)

Z=interpolation(x,y,test)
print (Z)


plt.contourf(x,y,Z)
#plot the coutour

plt.show()




