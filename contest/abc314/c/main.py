N, M = map(int, input().split())
S = input()
C = list(map(int, input().split()))

# 各色について、その色で塗られた文字の位置を記録する
color_positions = [[] for _ in range(M)]
for i, c in enumerate(C):
    color_positions[c - 1].append(i)

# 各色について、右に1つ巡回シフトする
for positions in color_positions:
    if positions:
        last = S[positions[-1]]
        for i in range(len(positions) - 1, 0, -1):
            S = S[:positions[i]] + S[positions[i - 1]] + S[positions[i] + 1:]
        S = S[:positions[0]] + last + S[positions[0] + 1:]

print(S)