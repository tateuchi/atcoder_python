N = int(input())
A = list(map(int, input().split()))

flag = True

for i in range(1, N):
    if A[i-1] != A[i]:
        flag = False
        break

print("Yes" if flag else "No")