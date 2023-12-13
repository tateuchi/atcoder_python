from sys import stdin

N=int(stdin.readline())
A=list(map(int,stdin.readline().split()))
D=int(stdin.readline())

left = [0]*(N+1)
right = [0]*(N+1)
for i in range(N):
    left[i+1] = max(left[i],A[i])
    right[-(i+2)] = max(right[-(i+1)],A[-(i+1)])

for i in range(D):
    L,R=map(int,stdin.readline().split())
    print(max(left[L-1], right[R]))