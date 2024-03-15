import sys
def I():
    return int(sys.stdin.readline())
def MI():
    return map(int, sys.stdin.readline().split())
def LI():
    return list(map(int, sys.stdin.readline().split()))

from math import *

N=I()

ans =[]
for i in range(1, 10**18):
    num = i**3
    if num > N:
        break
    tmp = num
    numr = 0
    while tmp > 0:
        numr = numr * 10 + tmp % 10
        tmp //= 10
    if num == numr:
        ans.append(num)

print(ans[-1])