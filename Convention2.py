from collections import defaultdict
from queue import PriorityQueue
import sys
from typing import Optional
from functools import total_ordering
import bisect

sys.stdin = open('convention2.in')
sys.stdout = open('convention2.out', 'w')


@total_ordering
class Cow:
    def __init__(self, priority, arrival, time_will_spend, ending_time):
        self.priority = priority
        self.arrival = arrival
        self.time_will_spend = time_will_spend
        self.ending_time = ending_time

    def __str__(self):
        return f'{self.priority}, {self.arrival}, {self.time_will_spend}, {self.ending_time}'

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.priority == other.priority



n = int(input())
cows = defaultdict(list)

lowest = 10**9
highest = 0
s = 0
for i in range(n):
    a, t = map(int, input().split())
    cows[a].append(Cow(i, a, t, None))
    lowest = min(lowest, a)
    s += t
    highest = max(highest, a)

keys = sorted(cows.keys())


answer = 0
queue = PriorityQueue()
current_cow = None
time = lowest
cows_served = 0
while cows_served < n:
    pos = bisect.bisect_right(keys, time)
    for times in keys[:pos]:
        keys.remove(times)
        for cow in cows.pop(times):
            queue.put(cow)
  
    if (current_cow is None or current_cow.ending_time <= time) and queue.qsize():
        current_cow = queue.get()
        answer = max(answer, time - current_cow.arrival)
        current_cow.ending_time = time + current_cow.time_will_spend
        time = current_cow.ending_time
        cows_served += 1
    elif not queue.qsize():
        pos = bisect.bisect_right(keys, time)
        if pos == -1:
            break
        time = keys[pos]

print(answer)
