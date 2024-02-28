N = int(input())
A = list(map(int, input().split()))

num = set()

for i in range(N):
    num.add(A[i])

num = sorted(num, reverse=True)

print(num[1])