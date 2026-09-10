import math
def func(x):
    return math.sqrt(1 - 0.4 * x**2) - math.asin(x)
r = 0.0
l = 1.0
eps = 0.00001

while (l - r) / 2 > eps:
    c = (l + r) / 2 
    if func(r) * func(c) < 0:
        r = c
    else:
        l = c
otvet = (r + l) / 2
print(otvet)
