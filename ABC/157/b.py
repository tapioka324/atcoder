A = list()
for _ in range(3):
    A.append(list(map(int, input().split())))

N = int(input())
B = list()
for _ in range(N):
    B.append(int(input()))

flag = [[False] * 3 for i in range(3)]
for b in B:
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                flag[i][j] = True
                break

ans = False
for i in range(3):
    if flag[i].count(True) == 3:
        ans = True
    if [f[i] for f in flag].count(True) == 3:
        ans = True
if flag[0][0] == flag[1][1] == flag[2][2] == True or flag[0][2] == flag[1][1] == flag[2][0] == True:
    ans = True

print('Yes' if ans else 'No')
