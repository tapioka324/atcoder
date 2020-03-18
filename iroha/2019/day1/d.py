N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)
X += sum(A[0::2])
Y += sum(A[1::2])
if X > Y:
    print('Takahashi')
elif X < Y:
    print('Aoki')
else:
    print('Draw')
