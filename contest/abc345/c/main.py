import sys
ri = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(ri())
mi = lambda: map(int, ri().split())
li = lambda: list(map(int, ri().split()))
mia = lambda *t: [f(ri()) for f in t]
bi = lambda n: [li() for _ in range(n)]


from collections import Counter

S=ri()
N=len(S)

C=Counter(S)
ans = N*(N-1)//2

for c in C.values():
  if c > 1:
    ans -= c*(c-1)//2

if len(set(S)) != len(S):
  ans += 1
print(ans)