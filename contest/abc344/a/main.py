import sys
ri = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(ri())
mi = lambda: map(int, ri().split())
li = lambda: list(map(int, ri().split()))
mia = lambda *t: [f(ri()) for f in t]
bi = lambda n: [li() for _ in range(n)]


def main():
   S=input()
   skip = False
   for s in S:
      if s == "|" and skip == False:
         skip = True
      elif s == "|" and skip == True:
         skip = False
      
      if skip == False and s != "|":
         print(s, end="")

   print()

   
if __name__ == "__main__":
   main()