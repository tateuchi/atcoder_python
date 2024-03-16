import sys
ri = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(ri())
mi = lambda: map(int, ri().split())
li = lambda: list(map(int, ri().split()))
mia = lambda *t: [f(ri()) for f in t]
bi = lambda n: [li() for _ in range(n)]


S=input()
for i in range(len(S)):
  if i == 0:
    if S[i] != "<":
      print("No")
      exit()
  elif i == len(S)-1:
    if S[i] != ">":
      print("No")
      exit()
  else:
    if S[i] != "=":
      print("No")
      exit()

print("Yes")