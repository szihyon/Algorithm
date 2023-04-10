# 입력값 받기 
r, c = map(int, input().split())
lst = [list(input()) for _ in range(r)]
# 상하좌우 탐색
directY = [-1, 0, 0, 1]
directX = [0, -1, 1, 0]

def dfs(y, x, cnt):
    global M_cnt
    # cnt최대값 갱신 
    if cnt > M_cnt:
        M_cnt = cnt
    
    # 상하좌우 탐색하기
    for i in range(4):
        dy = directY[i] + y
        dx = directX[i] + x
        # 범위 벗어나면 continue
        if dy < 0 or dx < 0 or dy > r-1 or dx > c-1: continue
        # 방문했던 곳이면 continue
        if visited[ord(lst[dy][dx])] == 1: continue
        # 방문체크하고
        visited[ord(lst[dy][dx])] = 1
        # dfs함수 실행, 매개변수로 cnt+1 넘겨주기
        dfs(dy, dx, cnt+1)
        # return하면서 방문체크 해제해주기
        visited[ord(lst[dy][dx])] = 0

# DAT 활용하기
visited = [0]*100
# 첫 시작점 
visited[ord(lst[0][0])] = 1
M_cnt = 0

dfs(0, 0, 1)
print(M_cnt)
