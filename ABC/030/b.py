n, m = map(int, input().split())
ans = abs(n % 12 * 30 + m * 0.5 - m * 6)
print(360 - ans if ans > 180 else ans)
