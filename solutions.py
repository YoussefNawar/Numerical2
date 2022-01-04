import numpy as num
import sys
n = input("Enter the number of variables : ")
def gauss_elimination(n):

     arr = num.zeros((n,n+1))
     xs = num.zeros(n)
     print("enter the coefficients")
     for i in range(n):
         for j in range(n + 1):
             arr[i][j] = float(input('a[' + str(i) + '][' + str(j) + ']='))
     for i in range(n):
         if arr[i][i] ==  0.0:
            print("divide by zero error")
            sys.exit()
     for i in range(n):
         for j in range(i+1,n):
             scale = arr[j][i] / arr[i][i]

             for k in range(n + 1):
                 arr[j][k] = arr[j][k] - scale * arr[i][k]
     xs[n - 1] = arr[n - 1][n] / arr[n - 1][n - 1]

     for i in range(n - 2, -1, -1):
         xs[i] = arr[i][n]

         for j in range(i + 1, n):
             xs[i] = xs[i] - arr[i][j] * xs[j]

         xs[i] = xs[i] / arr[i][i]
     return xs

gauss_elimination(3)


