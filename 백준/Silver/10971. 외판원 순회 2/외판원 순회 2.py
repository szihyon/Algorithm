N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
minV = float('inf')  # 더 큰 값을 초기 최소값으로 설정
visited = [False] * N  # 방문 여부를 추적하는 배열

def dfs(start, now, value, count):
    global minV
    if count == N and lst[now][start] > 0:  # 모든 도시를 방문하고 출발 도시로 돌아올 수 있는 경우
        minV = min(minV, value + lst[now][start])
        return
    for i in range(N):
        if lst[now][i] > 0 and not visited[i]:  # 방문하지 않은 도시이고, 이동 가능한 경우
            visited[i] = True
            dfs(start, i, value + lst[now][i], count + 1)
            visited[i] = False  # 다른 경로를 위해 방문 상태 초기화

for i in range(N):
    visited[i] = True
    dfs(i, i, 0, 1)
    visited[i] = False

print(minV)