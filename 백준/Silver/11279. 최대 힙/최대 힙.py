import heapq
import sys
input = sys.stdin.readline

N = int(input())
h = []

for i in range(N):
    n = int(input())
    if n == 0:
        if h:
            print(-1 * heapq.heappop(h))
        else:
            print(0)
    else:
        heapq.heappush(h, -n)