from collections import deque
T = int(input())

def bfs(start):
    global cnt
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        for i in range(N+1):
            if graph[now][i] == 1 and visit[i] == 0:
                if i == start:
                    cnt += 1
                    return
                visit[i] = 1
                q.append(i)


for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    graph = [[0]*(N+1) for _ in range(N+1)]
    visit = [0]*(N+1)
    cnt = 0
    for i in range(1, N+1):
        graph[i][nums[i-1]] = 1
    for i in range(1, N+1):
        if visit[i] == 0:
            bfs(i)
    print(cnt)