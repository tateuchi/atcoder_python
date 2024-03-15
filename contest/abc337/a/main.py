import sys
ri = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(ri())
mi = lambda: map(int, ri().split())
li = lambda: list(map(int, ri().split()))
mia = lambda *t: [f(ri()) for f in t]
bi = lambda n: [li() for _ in range(n)]


def main():
   N=ii()
   T,A=0,0
   for _ in range(N):
      X,Y=mi()
      T += X
      A += Y
   
   if T == A:
      print("Draw")
   elif T > A:
      print("Takahashi")
   else:
      print("Aoki")


if __name__ == "__main__":
   main()