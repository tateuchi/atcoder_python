H, W = map(int, input().split())
S = [input() for _ in range(H)]

count = 0
for i in range(H):
    for j in range(W):
        if i == 0:
            
        if S[i][j] == "#":
            count += 1

print(count)