N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

G = [[] for _ in range(N)]
for i in range(M):
    G[A[i] - 1].append(B[i] - 1)
    G[B[i] - 1].append(A[i] - 1)
col = [-1] * N

def func(v, c):
    col[v] = c
    for w in G[v]:
        if col[w] == c:
            return False
        if col[w] == -1 and not func(w, 1 - c):
            return False
    return True

ans = True
for i in range(N):
    if col[i] == -1:
        ans &= func(i, 0)
print('Yes' if ans else 'No')