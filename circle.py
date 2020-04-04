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
        a = test[n][0]
        b = test[n][1]
        r = 1
        theta = np.arange(0, 0.25 * np.pi, 0.01)
        x = a + r * np.cos(theta)
        y = b + r * np.sin(theta)
        x = np.around(x, decimals=2)
        y = np.around(y, decimals=2)
        c = [x,y] # can not get the right c like {[x1,y1],[x2,y2].....}
         

        print(c)
        c=np.unique(c)
        print(c)
