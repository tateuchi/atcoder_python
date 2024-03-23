import sys
ri = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(ri())
mi = lambda: map(int, ri().split())
li = lambda: list(map(int, ri().split()))
mia = lambda *t: [f(ri()) for f in t]
bi = lambda n: [li() for _ in range(n)]


N=ii()
S=set()

ans = "Yes"
for i in range(N):
  s=ri()
  first_flag = s[0] == "H" or s[0] == "D" or s[0] == "C" or s[0] == "S"
  second_flag = s[1] == "A" or s[1] == "2" or s[1] == "3" or s[1] == "4" or s[1] == "5" or s[1] == "6" or s[1] == "7" or s[1] == "8" or s[1] == "9" or s[1] == "T" or s[1] == "J" or s[1] == "Q" or s[1] == "K"
  third_flag = s in S
  if first_flag and second_flag and not third_flag:
    S.add(s)
  else:
    ans = "No"
    break

print(ans)