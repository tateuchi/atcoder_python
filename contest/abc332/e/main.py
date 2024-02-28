from itertools import combinations
import numpy as np

N, D = map(int, input().split())
W = list(map(int, input().split()))

def calculate_variance(weights, D):
    mean = sum(weights) / D
    variance = sum((x - mean) ** 2 for x in weights) / D
    return variance

def generate_combinations(weights, D):
    if D == 1:
        return [weights]
    else:
        for i in range(1, len(weights)):
            for combo in combinations(weights, i):
                remaining_weights = list(set(weights) - set(combo))
                for other_combos in generate_combinations(remaining_weights, D - 1):
                    yield [list(combo)] + other_combos

# 最小分散を求める
min_variance = float('inf')
for combo in generate_combinations(W, D):
    total_weights = [sum(bag) for bag in combo]
    variance = calculate_variance(total_weights, D)
    min_variance = min(min_variance, variance)

print(min_variance)
