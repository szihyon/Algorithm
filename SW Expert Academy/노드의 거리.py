# 풀이 1
# DFS
T = int(input())


def abc(S, cnt, G):
    global min

    if cnt > min: return

    if S == G:
        if cnt < min:
            min = cnt
        return min

    for i in range(len(lst)):
        if lst[S][i] == 1 and used[i] == 0:
            used[i] = 1
            abc(i, cnt + 1, G)
            used[i] = 0


for tc in range(1, T + 1):
    V, E = map(int, input().split())
    lst = [[0] * (V) for _ in range(V)]
    for i in range(E):
        r1, r2 = map(int, input().split())
        r1 = r1 - 1
        r2 = r2 - 1
        lst[r1][r2] = 1
        lst[r2][r1] = 1
    S, G = map(int, input().split())
    S = S - 1
    G = G - 1
    used = [0] * V
    min = 21e8
    used[S] = 1
    res = abc(S, 0, G)

    if min == 21e8:
        print(f"#{tc} 0")
    else:
        print(f"#{tc} {min}")



#######################################################################

# 풀이2
# BFS
from collections import deque

T = int(input())

def bfs(st):
    cnt = 0
    q = deque()
    q.append((st, 0))   # 첫 시작점의 위치와 이동거리(cnt)

    while q:
        now, cnt = q.popleft()  # 왼쪽부터 원소 꺼내기. 현재 위치와 이동 거리(cnt) 할당
        if G == now:    # 도착지와 현재 위치가 같으면 cnt 리턴
            return cnt

        for i in range(len(lst)):
            if lst[now][i] == 1 and used[i] == 0:   # 경로표시가 되어있고, 아직 방문하지 않은 곳이면 
                used[i] = 1 # 방문체크 후 
                q.append((i, cnt+1))    # 노드번호와 이동거리(+1) 추가 

    return 0


for tc in range(1, T+1):
    V, E = map(int, input().split())
    lst = [[0]*V for _ in range(V)]
    for i in range(E):
        r1, r2 = map(int, input().split())
        r1 = r1-1
        r2 = r2-1
        lst[r1][r2] = 1
        lst[r2][r1] = 1
    S, G = map(int, input().split())
    S = S-1
    G = G-1
    used = [0]*V
    used[S] = 1     # 첫 시작점 경로 1로 바꿔주기

    res = bfs(S)    # bfs함수 실행

    if res:
        print(f"#{tc} {res}")
    else:
        print(f"#{tc} 0")


