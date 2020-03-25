N = int(input())
A = list(map(int, input().split()))
ans = 0
m = 0
for i in range(N):
    if m < A[i]:
        m = A[i]
        ans += 1
print(ans)
