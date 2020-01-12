# -*- coding: utf-8 -*-

a, b = map(int, input().split())

if 0 < a <= b:
    ans = 'Positive'
elif a <= b < 0:
    if (b - a + 1) % 2 == 0:
        ans = 'Positive'
    else:
        ans = 'Negative'
else:
    ans = 'Zero'

print(ans)
