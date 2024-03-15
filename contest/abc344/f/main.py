import sys
ri = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(ri())
mi = lambda: map(int, ri().split())
li = lambda: list(map(int, ri().split()))
mia = lambda *t: [f(ri()) for f in t]
bi = lambda n: [li() for _ in range(n)]


def main():
   N=ii()
   P=bi(N)
   R=bi(N)
   D=bi(N-1)
   print(P)
   print(R)
   print(D)
   


if __name__ == "__main__":
   main()