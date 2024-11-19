# Source: https://usaco.guide/general/io
import sys
sys.stdin = open('gymnastics.in')
sys.stdout = open('gymnastics.out', 'w')

k, n = map(int, input().split())

rounds = [list(map(int, input().split())) for _ in range(k)]
pairs = 0
for i in range(1, n+1):
	for j in range(1, n+1):
		if i == j:
			continue
		is_pair = True
		for round in rounds:
			if round.index(i) > round.index(j):
				is_pair = False

		if is_pair:
			pairs += 1

print(pairs)
