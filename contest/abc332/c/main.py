N, M = map(int, input().split())
S = input()

plain_tshirts = M
logo_tshirts = 0
used_logo_tshirts = 0

for i in range(N):
    if S[i] == "0":
        plain_tshirts = M
        logo_tshirts = max(logo_tshirts, used_logo_tshirts)
        used_logo_tshirts = 0
    elif S[i] == "1":
        if plain_tshirts > 0:
            plain_tshirts -= 1
        else:
            used_logo_tshirts += 1
    elif S[i] == "2":
        used_logo_tshirts += 1

logo_tshirts = max(logo_tshirts, used_logo_tshirts)

print(max(0, logo_tshirts))
