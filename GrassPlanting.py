from collections import defaultdict
import sys

sys.stdin = open('planting.in')
sys.stdout = open('planting.out', 'w')

n = int(input())
connections = defaultdict(int)

for _ in range(n-1):
    a, b = map(int, input().split())
    connections[a] += 1
    connections[b] += 1

max_connections = 0
for v in connections.values():
    max_connections = max(max_connections, v+1)

print(max_connections)
