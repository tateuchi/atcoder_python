N, Q = map(int, input().split())
A = list(map(int, input().split()))
L, R = [], []
for _ in range(Q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

S = [0] * (N+1)

for i in range(1, N+1):
    S[i] += S[i - 1] + A[i-1]

for j in range(Q):
    print(S[R[j]] - S[L[j] - 1])
