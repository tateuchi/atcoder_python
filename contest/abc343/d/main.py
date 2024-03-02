import sys
def I():
    return int(sys.stdin.readline())
def MI():
    return map(int, sys.stdin.readline().split())
def LI():
    return list(map(int, sys.stdin.readline().split()))


N,T=MI()
AB=[LI() for _ in range(T)]

D={0: N}
S=[0]*N
ans = []
for i in range(T):
    A,B=AB[i]
    old_score = S[A-1]
    new_score = old_score + B
    S[A-1] += B
    if new_score in D:
        D[new_score] += 1
    else:
        D[new_score] = 1
    
    if D[old_score] == 1:
        D.pop(old_score)
    else:
        D[old_score] -= 1
    
    ans.append(len(D))

for a in ans:
    print(a)