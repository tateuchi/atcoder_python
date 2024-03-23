import sys
ri = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(ri())
mi = lambda: map(int, ri().split())
li = lambda: list(map(int, ri().split()))
mia = lambda *t: [f(ri()) for f in t]
bi = lambda n: [li() for _ in range(n)]


W,B=mi()
S="wbwbwwbwbwbw"
N=len(S)
ans = "No"
for i in range(N):
  w_cnt=0
  b_cnt=0
  for j in range(200):
    if S[(i+j)%N]=="w":
      w_cnt+=1
    else:
      b_cnt+=1
    if w_cnt==W and b_cnt==B:
      ans = "Yes"
      break
    if w_cnt>W or b_cnt>B:
      break
  if ans=="Yes":
    break
print(ans)