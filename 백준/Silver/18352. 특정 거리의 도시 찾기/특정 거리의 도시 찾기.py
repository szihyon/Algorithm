from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B) #단방향

answer = []

def bfs(start):
    visit = [0]*(N+1)
    queue = deque([(start, 0)])
    visit[start] = 1

    while queue:
        now, dist = queue.popleft()
        if dist == K:
            answer.append(now)
            continue
        for nxt in graph[now]: 
            if visit[nxt] == 1: continue
            visit[nxt] = 1
            queue.append((nxt, dist+1)) 

bfs(X)

if answer:
    answer.sort()
    for a in answer:
        print(a)
else:
    print(-1)