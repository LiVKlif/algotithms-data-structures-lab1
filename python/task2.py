import math
def func(x):
    return math.sqrt(1 - 0.4 * x**2) - math.asin(x)
l = 0.0
r = 1.0
eps = 0.00001
steps = 0
while 1:
  steps += 1
  c = l - func(l) * (r - l) / (func(r) - func(l))
  if abs(func(c)) < eps:
    break
  if func(l) * func(c) < 0:
    r = c
  else:
    l = c
  if step > 1000:
    break
print(c)
