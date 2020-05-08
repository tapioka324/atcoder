N, K = map(int, input().split())
A = [0] * N
for _ in range(K):
    d = int(input())
    for i in map(int, input().split()):
        A[i - 1] = 1
print(A.count(0))
