import math

def f(n, r):
    if n < 2:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N, M = map(int, input().split())
print(f(N, 2) + f(M, 2))
