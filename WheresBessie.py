# Source: https://usaco.guide/general/io
# misses last 3 test cases
# im too lazy to reduce time complexity an order of magnitude

from collections import defaultdict
import sys
sys.stdin = open('where.in')
sys.stdout = open('where.out', 'w')
n = int(input())
grid = [list(input()) for _ in range(n)]

def floodfill(x, y, bounds, segment, visited, letter):
    xleft, xright, ybottom, ytop = bounds
    if x < xleft or x > xright or y < ybottom or y > ytop:
        return
    if grid[x][y] != letter:
        return
    if (x, y) in visited:
        return

    segment.add((x, y))
    visited.add((x, y))

    floodfill(x+1, y, bounds, segment, visited, letter)
    floodfill(x-1, y, bounds, segment, visited, letter)
    floodfill(x, y+1, bounds, segment, visited, letter)
    floodfill(x, y-1, bounds, segment, visited, letter)


def is_pcl(x1, y1, x2, y2):
    colors = defaultdict(int)
    visited = set()
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if (x, y) in visited:
                continue
            segment = set()
            floodfill(x, y, (x1, x2, y1, y2), segment, visited, grid[x][y])
            colors[grid[x][y]] += 1

    if len(colors) > 2:
        return False
    
    one = False
    more = False

    for amount in colors.values():
        if amount == 1:
            one = True
        if amount > 1:
            more = True
        
    return one and more


pcls = []
for x1 in range(n):
    for y1 in range(n):
        for x2 in range(x1, n):
            for y2 in range(y1, n):
                if is_pcl(x1, y1, x2, y2):
                    pcls.append((x1, y1, x2, y2))


def is_inside(pcl1, pcl2):
    return pcl1[0] >= pcl2[0] and pcl1[1] >= pcl2[1] and pcl1[2] <= pcl2[2] and pcl1[3] <= pcl2[3]

ans = 0
for pcl1 in pcls:
    works = True
    for pcl2 in pcls:
        if pcl1 == pcl2:
            continue
        if is_inside(pcl1, pcl2):
            works = False
    if works:
        ans += 1

print(ans)
    
