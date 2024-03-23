import sys
ri = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(ri())
mi = lambda: map(int, ri().split())
li = lambda: list(map(int, ri().split()))
mia = lambda *t: [f(ri()) for f in t]
bi = lambda n: [li() for _ in range(n)]


N=ii()
S=ri()
C=li()

