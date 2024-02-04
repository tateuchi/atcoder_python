N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

A = [0] + A
B = [0, 0] + B

dp = [0]*N
dp[1] = A[1]
for i in range(2, N):
    dp[i] = min(dp[i-1]+A[i], dp[i-2]+B[i])

Place = N
ans = [Place]
while Place > 1:
    if dp[Place-2] + A[Place-1] == dp[Place-1]:
        Place -= 1
    else:
        Place -= 2
    ans.append(Place)

print(len(ans))
print(*ans[::-1])