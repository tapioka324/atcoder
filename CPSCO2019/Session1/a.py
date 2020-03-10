import math

N, A = map(int, input().split())

print(math.ceil(A / 3), min(N // 3, A))
