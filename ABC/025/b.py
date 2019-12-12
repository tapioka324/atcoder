# -*- coding: utf-8 -*-

N, A, B = map(int, input().split())
S = list()
D = list()
for _ in range(N):
    s, d = map(str, input().split())
    S.append(s)
    D.append(int(d))

ans = 0
for s, d in zip(S, D):
    if d < A:
        dist = A
    elif A <= d <= B:
        dist = d
    else:
        dist = B

    if s == 'East':
        ans += dist
    else:
        ans -= dist

if ans == 0:
    print('0')
elif ans > 0:
    print('East', ans)
else:
    print('West', abs(ans))
