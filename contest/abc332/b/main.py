K, G, M = map(int, input().split())
 
g, m = 0, 0
for _ in range(K):
    if g == G:
        g = 0
    elif m == 0:
        m = M
    else:
        g = min(g + m, G)
        m = max(m - g, 0)

print(g, m)