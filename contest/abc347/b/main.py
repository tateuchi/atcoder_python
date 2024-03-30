import sys
ri = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(ri())
mi = lambda: map(int, ri().split())
li = lambda: list(map(int, ri().split()))
mia = lambda *t: [f(ri()) for f in t]
bi = lambda n: [li() for _ in range(n)]

from itertools import combinations

S=list(ri())
ans=set()
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        ans.add("".join(S[i:j]))

print(len(ans))