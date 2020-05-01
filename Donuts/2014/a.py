N = int(input())
A = list(map(int, input().split()))
if N % 2 == 1:
    print('error')
    exit()
print(sum([A[i * 2 + 1] - A[i * 2] for i in range(N // 2)]))
