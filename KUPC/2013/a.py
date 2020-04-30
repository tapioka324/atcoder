N, Q = map(int, input().split())
ans = 'kogakubu10gokan'
for _ in range(N):
    y, n = map(str, input().split())
    if int(y) <= Q:
        ans = n
print(ans)
