N, S, M, L = map(int, input().split())

ans = 0
INF = 10**9
dp = [INF]*(N+12)    
dp[0] = 0

for i in range(N):
    dp[i+6] = min(dp[i+6], dp[i]+S)
    dp[i+8] = min(dp[i+8], dp[i]+M)
    dp[i+12] = min(dp[i+12], dp[i]+L)

print(min(dp[N:N+12]))