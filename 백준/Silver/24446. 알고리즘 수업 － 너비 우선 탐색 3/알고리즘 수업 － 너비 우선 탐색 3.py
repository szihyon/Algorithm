from collections import deque

N, M, R = map(int, input().split())
lst = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)

def bfs(start):
    q = deque([start])
    visit = [-1] * (N+1)  # -1로 초기화하여 방문하지 않은 상태를 표시
    visit[start] = 0  # 시작점의 거리는 0

    while q:
        now = q.popleft()
        for node in lst[now]:
            if visit[node] == -1:  # 방문하지 않은 정점
                visit[node] = visit[now] + 1
                q.append(node)
    return visit

# 시작점 R에서 BFS를 실행하여 모든 정점까지의 거리 계산
distances = bfs(R)

# 각 정점까지의 거리(깊이) 출력
for i in range(1, N+1):
    print(distances[i])
