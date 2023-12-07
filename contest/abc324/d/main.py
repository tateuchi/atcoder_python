import itertools

N = int(input())
S = sorted(list(input()))

num_set = set()
for it in itertools.permutations(S, N):
    num_set.add(int("".join(it)))

print(len(num_set))