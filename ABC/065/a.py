# -*- coding: utf-8 -*-

# input
X, A, B = map(int, input().split())

# solve
if B - A <= 0:
    ans = 'delicious'
elif B - A <= X:
    ans = 'safe'
else:
    ans = 'dangerous'

# output
print(ans)
