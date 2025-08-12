import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
lst = [[] for _ in range(N+1)]

for _ in range(N-1):
    A, B, C = map(int, input().split())
    lst[A].append((B, C))
    lst[B].append((A, C))

visit = [0]*(N+1)
maxV = 0
def dfs(now, total_distance):
    global maxV
    if total_distance > maxV:
        maxV = total_distance
    for next, distance in lst[now]:
        if visit[next] == 1: continue
        visit[next] = 1
        dfs(next, total_distance+distance)
        visit[next] = 0

visit[1] = 1
dfs(1, 0)
print(maxV)