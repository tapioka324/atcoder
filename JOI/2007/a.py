S = sum(list(map(int, input().split())))
T = sum(list(map(int, input().split())))
print(max(S, T) if S != T else S)
