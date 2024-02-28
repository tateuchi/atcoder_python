N, M = map(int, input().split())
A = list(map(int, input().split()))

P = [0]*N
remaining = [[] for _ in range(N)]

for i in range(N):
    S = input()
    for j in range(M):
        if S[j] == 'o':
            P[i] += A[j]
        else:
            remaining[i].append(j)

    P[i] += i+1

ans = []
maxP = max(P)
for i in range(N):
    count = 0

    # 関連するAの値を取り出す
    related_A = [A[j] for j in remaining[i]]

    # 関連するAの値を降順にソートする
    related_A.sort(reverse=True)

    # ソートされた関連するAの値を使用してPを更新する
    for a in related_A:
        if P[i] >= maxP:
            break
        P[i] += a
        count += 1
    ans.append(count)

print(*ans, sep="\n")
