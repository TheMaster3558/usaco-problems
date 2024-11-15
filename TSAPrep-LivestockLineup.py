from collections import defaultdict
from itertools import permutations

import sys
sys.stdin = open('lineup.in')
sys.stdout = open('lineup.out', 'w')

COWS = sorted(['Bessie', 'Buttercup', 'Belinda', 'Beatrice', 'Bella', 'Blue', 'Betsy', 'Sue'])

n = int(input())

contraints = defaultdict(list)
for _ in range(n):
    splitted = input().split()
    contraints[splitted[-1]].append(splitted[0])

for perm in permutations(COWS, len(COWS)):
    perm = list(perm)
    dont_work = False
    
    for cow, other_cows in contraints.items():
        index = perm.index(cow)

        if index == 0 and len(other_cows) > 1:
            dont_work = True
        elif index == len(perm) - 1 and len(other_cows) > 1:
            dont_work = True
        else:
            for other_cow in other_cows:
                if index == 0:
                    if perm[index+1] != other_cow:
                        dont_work = True
                elif index == len(perm) - 1:
                    if perm[index-1] != other_cow:
                        dont_work = True
                else:
                    if perm[index-1] != other_cow and perm[index+1] != other_cow:
                        dont_work = True


            
    if not dont_work:
        print('\n'.join(perm))
        exit(0)
