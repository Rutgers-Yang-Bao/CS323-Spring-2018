
import math;

def fun(x,a,num) :
    X = x;
    A = a;
    n = num;
    B = [];
    C = [];
    D = [];
    H = [];
    Alpha = [];
    Alpha.append(0);
    # Step 1 :
    for i in range(0,n):
        H.append(X[i+1] - X[i])

    # Step 2 :
    for i in range(1,n):
        Alpha.append((3/H[i])*(A[i+1]-A[i]) - (3/H[i-1])*(A[i]-A[i-1]))

    # Step 3 :
    L = [];
    U = [];
    Z = [];
    L.append(1);
    U.append(0);
    Z.append(0);

    # Step 4 :
    for i in range(1,n):
        L.append(2*(X[i+1]-X[i-1])-H[i-1]*U[i-1]);
        U.append(H[i]/L[i]);
        Z.append((Alpha[i]-H[i-1]*Z[i-1])/L[i]);

    # Step 5 :
    L.append(1);
    C.append(0);
    Z.append(0);

    # Step 6 :
    for i in range(0,n):
        j = n - 1 - i;
        C.append(Z[j]-U[j]*C[i]);
        B.append((A[j+1]-A[j])/H[j]-H[j]*(C[i]+2*C[i+1])/3);
        D.append((C[i]-C[i+1])/(3*H[j]));

    C.reverse();
    B.reverse();
    D.reverse();

    return [A,B,C,D]
