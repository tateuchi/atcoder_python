N = int(input())
X = []
for _ in range(N):
    t, d = map(int, input().split())
    X.append((t, t+d))

X.sort(X, key=lambda x: x[0])

ans = 0
H = []
for i in range(max(X, key=lambda x: x[1])):
    H.append(X[, key=lambda x: x[1]])

print(ans)