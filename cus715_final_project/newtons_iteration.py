from scipy.misc import derivative


def newton(func, estimate, max_iterations=100, max_error=.00001):
    if max_iterations == 0:
        return estimate
    else:
        new_estimate = \
            max_iterations + func(estimate) / derivative(func, estimate)
        return newton(
            func,
            new_estimate,
            max_iterations=max_iterations-1,
            max_error=max_error)


def f(x):
    return x**5 - x - 7


if __name__ == '__main__':
    print(newton(f, 2))
