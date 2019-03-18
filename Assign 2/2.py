X = [0.9, 1.3, 1.9, 2.1, 2.6, 3.0, 3.9, 4.4, 4.7, 5.0, 6.0, 7.0, 8.0, 9.2, 10.5, 11.3, 11.6, 12.0, 12.6, 13.0, 13.3]  # Make an array of x values  
y = [1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3, 2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4, 0.25]  # Make an array of y values for each x value  

print("input the value of n");

n = 20

F = [([0] * (n+1)) for i in range(n+1)]



for i in range(0,n+1):
    
    F[i][0] = y[i];

for i in range(1,n+1):
   for j in range (1,i+1):
       F[i][j] = (F[i][j-1] - F[i-1][j-1])/(X[i]-X[i-j]);

for i in range(1,n+1):
    print("{0}&{1}\\\\".format(i,F[i][i]));
