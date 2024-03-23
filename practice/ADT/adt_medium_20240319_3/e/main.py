import sys
ri = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(ri())
mi = lambda: map(int, ri().split())
li = lambda: list(map(int, ri().split()))
mia = lambda *t: [f(ri()) for f in t]
bi = lambda n: [li() for _ in range(n)]


S=ri()
cnt=0
i=0
while i < len(S):
  if S[i] == "0" and i + 1 < len(S): 
    if S[i+1] == "0":
      i += 1
  i += 1
  cnt += 1
  
print(cnt)