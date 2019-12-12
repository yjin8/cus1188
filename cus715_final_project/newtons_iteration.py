from scipy.misc import derivative
from math import ceil
import numpy as np

# basic newton iteration algorithm
def newton(func, estimate, min_error=.0001):
    diff = func(estimate)/derivative(func, estimate)
    while abs(diff) > min_error:
        diff = func(estimate)/derivative(func, estimate)
        estimate = estimate - diff
        diff = func(estimate)/derivative(func, estimate)
    return estimate


def f(x):
    return x**5 - x - 7
def y(x):
    return x**5 - 1000

'''
def InvertSeries(ma):
    n = len(ma)
    if n==1:
        return [-1/ma[0]]
    k = -(-n//2) # ceil(n/2)
    s = InvertSeries(ma[:k])+[0]*(n-k)
    t = Mul(ma,s,n) # -a*s
    t[0] += 1 # 1-a*s
    return Add(s,Mul(s,t,n))# s+s(1-a*s)
def NewtonInvert(a):
    return InvertSeries(ScalarMul(-1,a))

'''
def invert_series(ma):
    n = len(ma)
    if n == 1:
        return [-1/ma[0]]
    k = -(-n//2) # int(ceil(n / 2))
    s = invert_series(ma[:k])+[0]*(n-k)
    # t = np.multiply(s, ma)
    t = Mul(ma, s, n)  # -a*s
    t[0] += 1  # 1-a*s
    return Add(s, Mul(s, t, n))  # s+s(1-a*s)


def newton_invert(a):
    return invert_series(np.multiply(-1, a))


def Mul(to_mult, lst, pos):
    lst[pos] = to_mult


def Add(arg1, arg2):
    return [arg1, arg2]


def ScalarMul(to_mult, matrix):
    return np.multiply(to_mult, matrix)
    # return [i*to_mult for i in lst]


if __name__ == '__main__':
    print("Estimating root of x^5 - x - 7: " + str(newton(f, 2.5)))
    # outputs 1.53548522912
    print("Estimating root of x^5 - 1000 or 1000^(1/5): " + str(newton(y, 3.5)))
    # outputs 3.98107170553
    # print(ScalarMul(-1, [1,2,4]))
    print(newton_invert([1,2,3]))
