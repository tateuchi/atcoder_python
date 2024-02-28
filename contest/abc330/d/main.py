N = int(input())
S = [input() for _ in range(N)]

count = 0

row_counts = [0] * N
col_counts = [0] * N

for i in range(N):
    for j in range(N):
        if S[i][j] == 'o':
            row_counts[i] += 1
            col_counts[j] += 1


for i in range(N):
    for j in range(N):
        if S[i][j] == 'o':
            count += (row_counts[i] - 1) * (col_counts[j] - 1)

print(count)
