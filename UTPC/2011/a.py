M, N = map(int, input().split())
ans = 0
for _ in range(M):
    ans = max(ans, sum(list(map(int, input().split()))))
print(ans)
