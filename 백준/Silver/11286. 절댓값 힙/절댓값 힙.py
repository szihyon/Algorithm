import heapq
import sys
input = sys.stdin.readline

h = []

N = int(input())
for i in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(h, (abs(x), x))
    else:
        if h:
            print(heapq.heappop(h)[1])
        else:
            print(0)