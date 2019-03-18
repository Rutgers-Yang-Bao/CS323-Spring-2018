import numpy as np  
import matplotlib.pyplot as plt
import NaturalSpline
import DividedDifferences

def funDD(xs,X,DD,n):
    answer = 0;
    for i in range(0,n+1):
        a = DD[i]
        b = 1
        if (i > 0):
            for j in range(0,i):
                b = b * (xs - X[j])
        answer = answer + a*b;
    return answer
  
x = [0.9, 1.3, 1.9, 2.1, 2.6, 3.0, 3.9, 4.4, 4.7, 5.0, 6.0, 7.0, 8.0, 9.2, 10.5, 11.3, 11.6, 12.0, 12.6, 13.0, 13.3]  # Make an array of x values  
y = [1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3, 2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4, 0.25]  # Make an array of y values for each x value  
n = 20;
# points plot
plt.plot(x, y,'ro')  # use pylab to plot x and y


#NaturalSpline plot

NS = NaturalSpline.fun(x,y,n)

for i in range(0,n):
    
    xn = np.linspace(x[i],x[i+1],10000)
    yn = [(NS[0][i] + NS[1][i]*(j - x[i]) + NS[2][i]*(j - x[i])**2 + NS[3][i]*(j - x[i])**3) for j in xn]
    plt.plot(xn, yn,'b')

#Divided Difference plot

DD = DividedDifferences.fun(x,y,n)
xd = np.linspace(x[0],x[20],10000)

plt.plot(xd,funDD(xd,x,DD,n),'g')

plt.show()
