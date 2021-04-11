import math


def factorial(n):
    factor = 1
    for k in range(1, n + 1):
        factor = factor * k
    return factor


def ex(n):
    k = 1
    e_add = 1
    e_x = 1
    while math.fabs(e_add) >= eps:
        e_add = (-1 ** k) * ((n ** k) / factorial(k))
        e_x += e_add
        k += 1
    return e_x


x = int(input("Type x: "))
eps = float(input("Type eps: "))
if 0 <= x <= 2:
    y = ex(x) + ex(2 * x)
elif x > 2:
    y = (1 / ex(x + 5)) - ex(x + 2)
print("y =", y)
