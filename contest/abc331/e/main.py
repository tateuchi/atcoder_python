N, M, L = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

bad = set()
for _ in range(L):
    c, d = map(int, input().split())
    bad.add((c-1, d-1))

ans = 0
for i in range(N):
    for j in range(M):
        if (i, j) not in bad:
            ans = max(ans, a[i] + b[j])

print(ans)