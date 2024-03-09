import sys
ri = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(ri())
mi = lambda: map(int, ri().split())
li = lambda: list(map(int, ri().split()))
mia = lambda *t: [f(ri()) for f in t]
bi = lambda n: [li() for _ in range(n)]


def main():
   A=[]
   for e in sys.stdin:
      A.append(e[:-1])
   N=len(A)

   for a in reversed(A):
      print(a)


if __name__ == "__main__":
   main()