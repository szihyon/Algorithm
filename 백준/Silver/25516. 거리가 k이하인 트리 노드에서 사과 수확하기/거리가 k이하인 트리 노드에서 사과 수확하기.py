import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, k = map(int, input().split())
lst = [[] for _ in range(n)]

for _ in range(n-1):
    p, c = map(int, input().split())
    lst[p].append(c)
apple = list(map(int, input().split()))

visit = [0]*n
answer = 0
def dfs(now, distance):
    global answer
    if distance > k:
        return
    if apple[now] == 1:
        answer += 1
    for next in lst[now]:
        if visit[next] == 1: return
        visit[next] = 1
        dfs(next, distance+1)
        visit[next] = 0

visit[0] = 1
dfs(0, 0)

print(answer)