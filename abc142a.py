mport sys
import math

n = input()
n = float(n)
ans = (n - math.floor(n / 2))
ans = ans / n
print(ans)
