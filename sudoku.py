import itertools
from collections import defaultdict

nums = {9,8,7,6,5,4,3,2,1}
sums = defaultdict(lambda:[])

for size in {2,3,4}:
    for combo in itertools.combinations(nums,size):
        print(combo)
        sums[sum(combo),size].append(combo)

print(sums)