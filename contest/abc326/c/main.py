
# dpテーブルの初期化
dp = [[0] * (W+1) for _ in range(N+1)]

# dpループ
for i in range(1, N+1):
    for j in range(1, W+1):
        # dpの更新処理
        dp[i][j] = ...

# 答えの出力
print(dp[N][W])
