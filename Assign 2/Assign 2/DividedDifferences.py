def fun(x,f,num):
    X = x;
    n = num;
    F = [([0] * (n+1)) for i in range(n+1)]
    answer = [];
    for i in range(0,n+1):
        F[i][0] = f[i]

    for i in range(1,n+1):
       for j in range (1,i+1):
           F[i][j] = (F[i][j-1] - F[i-1][j-1])/(X[i]-X[i-j]);

    for i in range(0,n+1):
        answer.append(F[i][i])
    return answer;
