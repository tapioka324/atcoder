# -*- coding: utf-8 -*-

# input
A = input()
B = input()
C = input()

# solve
turn = 'a'
while True:
    if turn == 'a':
        if A:
            turn = A[0]
            A = A[1:]
        else:
            ans = 'A'
            break
    elif turn == 'b':
        if B:
            turn = B[0]
            B = B[1:]
        else:
            ans = 'B'
            break
    else:
        if C:
            turn = C[0]
            C = C[1:]
        else:
            ans = 'C'
            break

# output
print(ans)
