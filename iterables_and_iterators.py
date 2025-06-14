# Task: iterables-and-iterators
from itertools import combinations
n = int(input())
letters = input().split()
k = int(input())
combs = list(combinations(letters, k))
count = sum(1 for c in combs if 'a' in c)
print("{0:.4f}".format(count / len(combs)))