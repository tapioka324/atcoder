L, X = map(int, input().split())

r = X % (2 * L)
print(r if r < L else 2 * L - r)
