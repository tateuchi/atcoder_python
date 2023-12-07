N, M, L = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

bad = set()
for _ in range(L):
    c, d = map(int, input().split())
    bad.add((c-1, d-1))

s = sorted([(p, j) for j, p in enumerate(b)], reverse=True)

ans = 0
for i in range(N):
    for p, j in s:
        if (i, j) not in bad:
            ans = max(ans, a[i] + p)
            break
print(ans)