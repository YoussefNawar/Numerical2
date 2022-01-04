import numpy as num
import sys

n = int(input("Enter the number of variables : "))


def gauss_elimination(n):
    arr = num.zeros((n, n + 1))
    xs = num.zeros(n)
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
    for i in range(n):
        if arr[i][i] == 0.0:
            print("divide by zero error")
            sys.exit()
    for i in range(n):
        for j in range(i + 1, n):
            m = arr[j][i] / arr[i][i]

            for k in range(n + 1):
                arr[j][k] = arr[j][k] - m * arr[i][k]

    xs[n - 1] = arr[n - 1][n] / arr[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        xs[i] = arr[i][n]

        for j in range(i + 1, n):
            xs[i] = xs[i] - arr[i][j] * xs[j]

        xs[i] = xs[i] / arr[i][i]
    print (xs)

def LU(n):
    arr = num.zeros((n, n + 1))
    xs = num.zeros(n)
    b = num.zeros(n)
    print("enter the coefficients:")
    for i in range(n):
        for j in range(n + 1):
            if j is not n:
                arr[i][j] = float(input('arr[' + str(i) + '][' + str(j) + ']='))
            else:
                arr[i][j] = float(input('b[' + str(i) + ']='))
    print(arr)
    for i in range(n - 1):
        for k in range(i + 1, n):
            if num.fabs(arr[k][0]) > num.fabs(arr[i][0]):
                arr[[i, k]] = arr[[k, i]]

    print(arr)
    L = num.zeros((n,n))

    U = num.zeros((n,n))
    for j in range (n):
        L[j][j] = 1
        s1 = 0.0
        for i in range(j + 1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = arr[i][j] - s1


        for i in range(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            L[i][j] = (arr[i][j] - s2) / U[j][j]
    for i in range (n):
        b[i] = arr[i][n]
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


    print(U)
    print(L)
    print(b)
    print(d)
    print(xs)
LU(n)