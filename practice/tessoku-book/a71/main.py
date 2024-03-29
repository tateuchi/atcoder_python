import sys
ri = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(ri())
mi = lambda: map(int, ri().split())
li = lambda: list(map(int, ri().split()))
mia = lambda *t: [f(ri()) for f in t]
bi = lambda n: [li() for _ in range(n)]

N=ii()
A=li()
B=li()

A.sort()
B.sort(reverse=True)
ans=0
for i in range(N):
  ans += A[i]*B[i]

print(ans)