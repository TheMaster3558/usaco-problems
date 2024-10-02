t = int(input())
for _ in range(t):
	n = int(input())
	sights = list(map(int, input().split()))
	prefix = [sights[0]]
	for i in range(1, len(sights)):
		if prefix[-1] - 1 > sights[i]:
			prefix.append(prefix[-1] - 1)
		else:
			prefix.append(sights[i])
	suffix = [0] * (len(sights) - 1)
	suffix.append(sights[-1])
	for i in range(-2, -len(suffix) - 1, -1):
		if suffix[i+1] - 1 > sights[i]:
			suffix[i] = suffix[i+1] - 1
		else:
			suffix[i] = sights[i]


	best = -1
	for i in range(1, len(sights)-1):
		best = max(best, prefix[i-1] + sights[i] + suffix[i+1] - 2)
	print(best)
