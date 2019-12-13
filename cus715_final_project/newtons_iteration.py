from scipy.misc import derivative


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


# newton iteration for division
def newton_div(a, min_error=.0001):
    k = 0
    while 10**k < a:
        k += 1
    init_estimate = 1/(10**k)
    estimate = init_estimate * (2 - (a * init_estimate))
    diff = estimate - init_estimate
    while min_error < abs(diff):
        old_estimate = estimate
        estimate = estimate * (2 - (a * estimate))
        diff = estimate - old_estimate
    return estimate


if __name__ == '__main__':
    print("Estimating root of x^5 - x - 7: " + str(newton(f, 2.5)))
    # outputs 1.53548522912
    print("Estimating root of x^5 - 1000 or 1000^(1/5): " + str(newton(y, 3.5)))
    # outputs 3.98107170553
    print("Estimating 1/115: ", newton_div(115))
    # outputs 0.008695650767733392
