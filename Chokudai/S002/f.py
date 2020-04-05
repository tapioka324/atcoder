N  = int(input())
s = set()
for _ in range(N):
    a, b = sorted(map(int, input().split()))
    s.add((a, b))
print(len(s))
