from collections import defaultdict
import sys

sys.stdin = open('factory.in')
sys.stdout = open('factory.out', 'w')

n = int(input())
edges = defaultdict(list)

for _ in range(n-1):
	a, b = map(int, input().split())
	edges[a].append(b)


def dfs(vertex, target, visited):
	if vertex in visited:
		return False
	if vertex == target:
		return True
	visited.add(vertex)
	return any(dfs(edge, target, visited) for edge in edges[vertex])


for i in range(1, n+1):
	can = True
	for j in range(1, n+1):
		if i != j:
			if not dfs(j, i, set()):
				can = False

	if can:
		print(i)
		exit(0)


print(-1)
