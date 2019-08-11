# -*- coding: utf-8 -*-

# input
A, B = map(int, input().split())

# solve
card = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
if card.index(A) > card.index(B):
    ans = 'Alice'
elif card.index(A) < card.index(B):
    ans = 'Bob'
else:
    ans = 'Draw'

# output
print(ans)
