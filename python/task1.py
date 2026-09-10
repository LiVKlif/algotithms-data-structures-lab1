import math
def func(x):
    return math.sqrt(1 - 0.4 * x**2) - math.asin(x)
l = 0.0
r = 1.0
eps = 0.00001

while (r - l) / 2 > eps:
  c = (l + r) / 2 
  if func(l) * func(c) < 0:
      r = c
  else:
      l = c
otvet = (r + l) / 2
print(otvet)
