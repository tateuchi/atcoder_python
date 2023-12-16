N=int(input())
A=list(map(int,input().split()))
A.sort()

Amin=A[0]
Amax=A[-1]

for i in range(Amin,Amin+N+1):
    if i not in A:
        print(i)
        exit()