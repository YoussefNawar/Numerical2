import numpy as num
import sys


def gauss_elimination(M):
    n = len(M)
    a = (num.array(M))
    a = a.astype(float)
    # arr = num.zeros((n, n + 1))
    xs = num.zeros(n)
    # print("enter the coefficients:")
    # for i in range(n):
    #     for j in range(n + 1):
    #         if j is not n:
    #            arr[i][j] = float(input('arr[' + str(i) + '][' + str(j) + ']='))
    #         else:
    #             arr[i][j] = float(input('b[' + str(i) + ']='))
    # print(arr)
    for i in range(n - 1):
        for k in range(i + 1, n):
            if num.fabs(a[k][0]) > num.fabs(a[i][0]):
                a[[i, k]] = a[[k, i]]

    print(a)
    for i in range(n):
        if a[i][i] == 0.0:
            print("divide by zero error")
            sys.exit()
    for i in range(n):
        for j in range(i + 1, n):
            m = a[j][i] / a[i][i]

            for k in range(n + 1):
                a[j][k] = a[j][k] - m * a[i][k]
    xs[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        xs[i] = a[i][n]

        for j in range(i + 1, n):
            xs[i] = xs[i] - a[i][j] * xs[j]

        xs[i] = xs[i] / a[i][i]
        # print(M)
    print(xs)
    return str(a), str(xs)


m2 = [[1, 1, -1, -3], [6, 2, 2, 2], [-3, 4, 1, 1]]
#gauss_elimination(m2)


def LU(M):
    #arr = num.zeros((n, n + 1))

    n = len(M)
    xs = num.zeros(n)
    b = num.zeros(n)
    a = num.array(M)
    a = a.astype(float)

    # for i in range(n):
    #     for j in range(n + 1):
    #         if j is not n:
    #             arr[i][j] = float(input('arr[' + str(i) + '][' + str(j) + ']='))
    #         else:
    #             arr[i][j] = float(input('b[' + str(i) + ']='))
    # print(arr)
    for i in range(n - 1):
        for k in range(i + 1, n):
            if num.fabs(a[k][0]) > num.fabs(a[i][0]):
                a[[i, k]] = a[[k, i]]

    #print(M)
    memo = "pivoted matrix = " + str(a)
    print(memo)
    L = num.zeros((n,n))

    U = num.zeros((n,n))
    for j in range (n):
        L[j][j] = 1
        s1 = 0.0
        for i in range(j + 1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = a[i][j] - s1


        for i in range(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            L[i][j] = (a[i][j] - s2) / U[j][j]
    for i in range (n):
        b[i] = a[i][n]
    d = num.zeros(n)
    for i in range(len(L)):  # forward substitution
        d[i] = b[i]
        for j in range(len(L[0])):
            if i != j:
                d[i] -= d[j] * L[i][j]
    for i in range(len(U) - 1, -1, -1):  # backward substitution
        xs[i] = d[i]
        for j in range(0, len(U[0])):
            if i != j:
                xs[i] -= xs[j] * U[i][j]
        xs[i] = xs[i] / U[i][i]


    uu = "U = " + str(U)
    ll ="L = " + str(L)
    bb ="b = " +  str(b)
    dd = "d = " + str(d)
    xx = "x-values: " + str(xs)
    print(uu)
    print(ll)
    print(bb)
    print(dd)
    print(xx)
    #final = ("pivoted array = " + M + "L = " + L + "U = " + U + "b = " + b + "d= " + d + "x values: " + xs)
    #print(final)
    return memo,uu,ll,bb,dd,xx
#LU(m2)
def jordan(M):
    n = len(M)
    a = num.array(M)
    a = a.astype(float)
    # arr = num.zeros((n, n + 1))
    xs = num.zeros(n)
    # print("enter the coefficients:")
    # for i in range(n):
    #     for j in range(n + 1):
    #         if j is not n:
    #             arr[i][j] = float(input('arr[' + str(i) + '][' + str(j) + ']='))
    #         else:
    #             arr[i][j] = float(input('b[' + str(i) + ']='))
    # print(arr)
    for i in range(n - 1):
        for k in range(i + 1, n):
            if num.fabs(a[k][0]) > num.fabs(a[i][0]):
                a[[i, k]] = a[[k, i]]
    memo = "pivoted matrix = " + str(a)
    print(memo)
    for i in range(n):
        if a[i][i] == 0.0:
            print("divide by zero error")
            sys.exit()
        for j in range(n):
            if i == j:
                #a = M[i][i]
                a[i] = a[i] / a[i][i]
            else:
                m1 = a[j][i] / a[i][i]


                for k in range(n + 1):
                    a[j][k] = a[j][k] - m1 * a[i][k]
    memo_jordan = "matrix after gauss jordan: " + str(a)
    print(memo_jordan)
    for i in range(n):
        xs[i] = a[i][n] / a[i][i]
    xx = "x-values : " + str(xs)
    print(xx)
    return memo,memo_jordan,xx

#jordan(m2)
def seidel(n,x,epsilon = 0.00001,iterations = 50):
    global s1
    arr = num.zeros((n, n + 1))
    xs = num.zeros(n)
    b = num.zeros(n)
    a = num.zeros((n,n))
    print("enter the coefficients:")
    for i in range(n):
        for j in range(n + 1):
            if j is not n:
                arr[i][j] = float(input('arr[' + str(i) + '][' + str(j) + ']='))
            else:
                arr[i][j] = float(input('b[' + str(i) + ']='))
    print(arr)
    for i in range(n-1):
        for k in range(i+1,n):
            if num.fabs(arr[k][0]) > num.fabs(arr[i][0]):
                arr[[i,k]] = arr[[k,i]]
    print(arr)
    for i in range (n):
        for j in range(n):
            a[i][j] = arr[i][j]

    print(a)
    for i in range (n):
        b[i] = arr[i][n]
    print(b)
    diag = num.diag(num.abs(a))

    # Find row sum without diagonal
    off_diag = num.sum(num.abs(a), axis=1) - diag

    if num.all(diag > off_diag):
        print('matrix is diagonally dominant')
    else:
        print('NOT diagonally dominant')
        sys.exit()
    iterationlist = []
    x_size = len(x)
    e = num.zeros(x_size)
    error = num.zeros(x_size)
    for i in range(x_size):
        iterationlist.append('x%d = %d'%(i,x[i]))

    for i in range(1,4):
        for j in range(n):
            s1 = 0
            for k in range(n):
                if k == j:
                    continue
                s1 = s1+(a[j][k]*x[k])
            #print(s1)
            x[j] = (b[j] - s1)/a[j][j]
            print(x[j])
    #print(iterationlist)
#seidel(n,[0,0,0],0.00001,50)