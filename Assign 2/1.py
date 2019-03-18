
import math;

x = [0.9, 1.3, 1.9, 2.1, 2.6, 3.0, 3.9, 4.4, 4.7, 5.0, 6.0, 7.0, 8.0, 9.2, 10.5, 11.3, 11.6, 12.0, 12.6, 13.0, 13.3]  # Make an array of x values  
y = [1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3, 2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4, 0.25]  # Make an array of y values for each x value  


X = [];
A = [];
B = [];
C = [];
D = [];
H = [];
Alpha = [];
Alpha.append(0);
    # Input step :
n = 20;

X = x;

A = y;

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
# Step 7 :
for i in range(0,n):
    print("{0}&{1}&{2}&{3}&{4}&{5}\\\\".format(i,X[i],A[i],B[i],C[i],D[i]));
