N  = int(input())
ans = 0
for _ in range(N):
    ans += max(map(int, input().split()))
print(ans)
