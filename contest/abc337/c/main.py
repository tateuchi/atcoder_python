import sys
ri = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(ri())
mi = lambda: map(int, ri().split())
li = lambda: list(map(int, ri().split()))
mia = lambda *t: [f(ri()) for f in t]
bi = lambda n: [li() for _ in range(n)]


from collections import defaultdict


def main():
   N=ii()
   A=li()
   D=dict()
   for i in range(N):
      if A[i] == -1:
         key = i + 1
      else:
         D[A[i]] = i + 1

   ans=[key]
   for _ in range(N-1):
      ans.append(D[key])
      key = D[key]
   
   print(*ans)

if __name__ == "__main__":
   main()