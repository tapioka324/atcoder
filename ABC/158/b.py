N, A, B = map(int, input().split())

ans = 0
if A == 0:
    print(ans)
    exit()

ans +=  N // (A + B) * A
ans += min(N % (A + B), A)

print(ans)
