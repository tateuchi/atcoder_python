from collections import deque

N = int(input())
G = [[] for _ in range(N)]
child_count = [0] * N

for _ in range(N-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[v].append(u)
    child_count[u] += 1

leaves = [i for i in range(N) if child_count[i] == 0]

if not G[0]:
    print(1)
    exit()

ans = 10**9
for leaf in leaves:
    current = leaf
    delete_count = 0
    while current != 0:
        if not G[current]:
            break
        delete_count += child_count[current]
        current = G[current][0]

    ans = min(ans, delete_count+2)

print(G)
print(leaves)
print(child_count)
print(ans)