S = input()

flag = True
for i in range(1, 16, 2):
    if S[i] == "1":
        flag = False
        break

print("Yes" if flag else "No")