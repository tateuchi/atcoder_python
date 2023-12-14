N,K=map(int,input().split())
A=list(map(int,input().split()))

def check(x):
    cnt = 0
    for a in A:
        cnt += x//a
    flag = cnt >= K
    return flag

L = 1
R = 10**5 + 1
while R > L:
    mid = (L + R)//2
    if check(mid):
        R = mid
    else:
        L = mid + 1

print(L)