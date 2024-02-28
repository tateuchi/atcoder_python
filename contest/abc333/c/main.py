N=int(input())

def generate_repunits(limit):
    repunits = []
    num = 1
    while len(repunits) < limit:
        repunits.append(num)
        num = num * 10 + 1
    return repunits

def nth_repunit_sum(N):
    repunits = generate_repunits(12)
    sums = set()

    for i in range(len(repunits)):
        for j in range(i, len(repunits)):
            for k in range(j, len(repunits)):
                sums.add(repunits[i] + repunits[j] + repunits[k])

    sorted_sums = sorted(list(sums))
    return sorted_sums[N - 1]

print(nth_repunit_sum(N))  # 例: N = 10
