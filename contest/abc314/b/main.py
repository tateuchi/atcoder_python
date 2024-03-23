import sys
ri = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(ri())
mi = lambda: map(int, ri().split())
li = lambda: list(map(int, ri().split()))
mia = lambda *t: [f(ri()) for f in t]
bi = lambda n: [li() for _ in range(n)]


N=ii()
C,A=[],[]
for _ in range(N):
  c=ii()
  a=li()
  C.append(c)
  A.append(a)
X=ii()

ans=[]
num = 38
for i in range(N):
  if X in A[i]:
    if num == C[i]:
      ans.append(i+1)
    elif num > C[i]:
      ans = [i+1]
      num = C[i]

ans.sort()
print(len(ans))
print(*ans)