from math import gcd
from itertools import accumulate

n = int(input())
array = list(map(int, input().split()))


prefix = list(accumulate(array, gcd))
suffix = list(reversed(list(accumulate(reversed(array), gcd))))

best = -1
for i in range(1,n-1):
    best = max(best, gcd(prefix[i-1], suffix[i+1]))


best = max(best, suffix[1])
best = max(best, prefix[n-2])

print(best)
