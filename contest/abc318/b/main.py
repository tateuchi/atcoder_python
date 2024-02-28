N = int(input())
G = [[False]*100 for _ in range(100)]

for _ in range(N):
    A, B, C, D = map(int, input().split())
    for i in range(C, D):
        for j in range(A, B):
            G[i][j] = True

count = sum(sum(g) for g in G)
print(count)
