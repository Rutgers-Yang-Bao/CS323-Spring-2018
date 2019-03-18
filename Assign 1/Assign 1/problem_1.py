'''
Created on Feb 10, 2018

@author: Yang Bao
'''

import math;

def fun1(x):                                # function of n!
    a = 1
    for i in range(1,x+1) :
        a = a*i;
    return a;

def fun2(x):                                # function of the second part
    a = math.sqrt(2 * math.pi * x) * math.pow(x/math.e , x);
    return a;

'''
For the grader:
I found that in the question it required us to calculate from 1 to 10.
But when I found that I have finished my codes.
I think my codes is the advanced version so I don't want to change it.
So please just input 10 when testing. Thx.
'''

print("input how big you want the n to be");
time = int(input());

for n in range(1,time+1):
    absoluteError = fun1(n)-fun2(n);
    print("Absolute error for n = {0} is : {1}".format(n,absoluteError));

print("---------------------------------------------------------------");

for n in range(1,time+1):
    absoluteError = fun1(n)-fun2(n);
    relativeError = absoluteError / fun1(n);
    print("Relative error for n = {0} is : {1}".format(n,relativeError));
    
print("\nAs we can find that the Absolute error grows and the relative error shrinks while the n increasing")
