'''
Created on Feb 10, 2018

@author: Yang Bao
'''
import math;

                
def funa(x):                                            # function of problem (a)
    return math.pow(math.e,x) - math.sin(x) - 2;

def ffuna(x):                                           # derivative function of (a)
    return math.pow(math.e,x) - math.cos(x);

def funb(x):                                            # function of problem (b)
    return math.pow(x, 2) - 4 * x + 4 - math.log(x);

def ffunb(x):                                           # derivative function of (b)
    return 2*x - 4 - 1/x;

errorbound = math.pow(10, -10);

# choose the function to solve
print("choose which function you want to solve :");
print("    1 for function (a)\n    2 for function (b)");
choice1 = int(input());

while (choice1 != 1 and choice1 != 2):                  # check if the input is correct
    print("Wrong input \n please input again");
    choice1 = int(input());
else:
    if(choice1 == 1):
        fun = funa;
        ffun = ffuna;
    elif(choice1 == 2):
        fun = funb;
        ffun = ffunb;
        
# choose the method to apply
print("choose which method you want to apply :");
print("    1 for bisection method \n    2 for Newton method \n    3 for secant method");
choice2 = int(input());
        
while(choice2 != 1 and choice2 != 2 and choice2 != 3):  # check if the input is correct
    print("Wrong input \n please input again")
    choice2 = int(input());
else:
    if(choice2 == 1):
        # codes for bisection method:
        print("input the initial a");
        a = float(input());
        print("input the initial b");
        b = float(input());   
        times = 0;

        while (fun(a) * fun(b) > 0):
            print("wrong input, there is no root in this interval");
            print("please input again");
            print("input the initial a");
            a = float(input());
            print("input the initial b");
            b = float(input());
        print("n      a      b     c     interval     f(c)");
        print("-----------------------------------------------------------");
        interval = b - a;
        while (interval >= errorbound) :
            c = (a + b) / 2;
            interval = b - c;
            print("{0}    {1}    {2}    {3}    {4}    {5}".format(times,a,b,c,interval,fun(c)));
            times = times + 1;
            if (fun(a) * fun(c) < 0):
                b = c;
            else:
                a = c;
        print("The root of the function is {0}".format(c));
    
    elif(choice2 == 2):
        # codes for Newton's method
        # I setup it runs no more than 20 iterations
        print("input the initial x");
        x = float(input());
        times = 0;
        print("n      x(n)      f(x)     f'(x)     x(n+1)     error");
        print("-----------------------------------------------------------");
        xx = x - fun(x)/ffun(x);
        error = math.fabs(x - xx);
        while( error > errorbound) :
            if(times < 21):
                xx = x - fun(x)/ffun(x);
                error = math.fabs(x - xx);
                print("{0}    {1}    {2}    {3}    {4}    {5}".format(times,x,fun(x),ffun(x),xx,error));
                x = xx;
                times = times + 1;
            else:
                print("The initial x is too far from the root, please check again");
                break;
        if (times < 21):
            print("The root of the function is {0}".format(x));
        
    elif(choice2 == 3):
        # codes for secant method
        # I setup it runs no more than 20 iterations
        print("input the initial x0");
        x0 = float(input());
        print("input the initial x1")
        x1 = float(input());
        print("n      x(n)      x(n+1)     x(n+2)     error");
        print("-----------------------------------------------------------");
        xx = x1 - fun(x1) * (x1 - x0) / (fun(x1)-fun(x0));
        error = math.fabs(xx - x1);
        times = 0;
        while( error > errorbound) :
            if(times < 21):
                xx = x1 - fun(x1) * (x1 - x0) / (fun(x1)-fun(x0));
                error = math.fabs(xx - x1);
                print("{0}    {1}    {2}    {3}    {4}".format(times,x0,x1,xx,error));
                x0 = x1
                x1 = xx;
                times = times + 1;
            else:
                print("The initial x is too far from the root, please check again");
                break;
        if (times < 21):
            print("The root of the function is {0}".format(xx));
