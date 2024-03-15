import sys
ri = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(ri())
mi = lambda: map(int, ri().split())
li = lambda: list(map(int, ri().split()))
mia = lambda *t: [f(ri()) for f in t]
bi = lambda n: [li() for _ in range(n)]


from collections import *


def main():
   S=ri()
   N=len(S)
   ABC="ABC"
   num = 0
   idx = 0
   i = 0
   while True:
      if idx == 3 or not i < N:
         break
      if ABC[idx] == S[i]:
         num += 1
         i += 1
      else:
         idx += 1

   if num == N:
      print("Yes")
   else:
      print("No")

if __name__ == "__main__":
   main()