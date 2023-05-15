import heapq
import sys
input = sys.stdin.readline

h = []

N = int(input())
for i in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(h, x)
    elif x == 0:
        if h:
            print(heapq.heappop(h))
        else:
            print(0)