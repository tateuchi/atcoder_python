N, M = map(int, input().split())
D = [[None] * N for _ in range(N)]
for i in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    D[A][B] = C
    D[B][A] = C

# グラフ理論で取り組もうという考えは間違っていなかった
# グローバル変数を用いるという考えがあまりなかった
# dfsの実装をどのようにするかというところが考えられなかった

ans = 0
visited = [False] * N

def dfs(v,count):
    global ans
    visited[v] = True
    if count > ans:
        ans = count

    for i in range(N):
        if not visited[i] and D[v][i] is not None:
            dfs(i, count + D[v][i])
    visited[v] = False

for i in range(N):
    dfs(i,0)

print(ans)