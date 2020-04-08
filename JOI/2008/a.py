N = 1000 - int(input())
ans = 0
for i in (500, 100, 50, 10, 5, 1):
    ans += N // i
    N %= i
print(ans)
