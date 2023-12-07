N ,M = map(int, input().split())
S = input()
T = input()

ans = 3

if (S == T[0:N]):
    ans -= 2
if (S == T[M-N:M]):
    ans -= 1

print(ans)

# S, T = [input(), input(), input()][1:]
# ans1 = T.startswith(S)
# ans2 = T.endswith(S)
# if ans1 and ans2:
#     print(0)
# elif ans1:
#     print(1)
# elif ans2:
#     print(2)
# else:
#     print(3)
