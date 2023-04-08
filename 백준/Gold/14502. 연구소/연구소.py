import copy
from collections import deque

n, m = map(int, input().split())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

# 바이러스의 확산
def bfs(stY, stX, lst2):
    # 상하좌우 방향배열 
    directY = [-1, 0, 0, 1]
    directX = [0, -1, 1, 0]
    
    q = deque()
    # 바이러스 시작점 q에 추가
    q.append((stY, stX))
    
    # q에 값이 남아 있지 않을 때까지 반복
    while q:
        # q에서 y,x좌표 하나씩 꺼내서 함수 실행 
        nowY, nowX = q.popleft()
        for i in range(4):
            dy = directY[i] + nowY
            dx = directX[i] + nowX
            # 현재 좌표에서 상하좌우를 탐색하고,
            # 배열 범위를 벗어나거나 값이 1이나 2인 경우는 pass
            if dy < 0 or dx < 0 or dy > n-1 or dx > m-1: continue
            if lst2[dy][dx] == 2: continue
            if lst2[dy][dx] == 1: continue
            # 0인 구역은 바이러스로 바꿔주고 q에 추가해주기
            lst2[dy][dx] = 1
            q.append((dy, dx))


# 벽을 3개 세우고 bfs실행하는 코드
def dfs(level, start):
    global M_cnt
    # 벽 세울 좌표 3개 골랐으면 bfs함수 실행하고 return
    if level == 3:
    
        # 초기 배열(lst) 복사해서 사용하기
        lst2 = copy.deepcopy(lst)
        cnt = 0
        
        # 벽 리스트(3개) 원소 하나씩 꺼내서 1로 바꿔주기
        for i in range(3):
            y, x = path[i]
            lst2[y][x] = 1
            
        # 바이러스(2)가 있는 곳에서 bfs함수 실행하기
        for i in range(len(lst2)):
            for j in range(len(lst2[i])):
                if lst2[i][j] == 2:
                    bfs(i, j, lst2)
                    
        # 바이러스 확산 모두 시킨 후, 안전 영역(0)구간 세주기
        for i in range(len(lst2)):
            for j in range(len(lst2[i])):
                if lst2[i][j] == 0:
                    cnt += 1
                    
        # 안전영역 크기가 최대값보다 크다면 갱신해주기
        if cnt > M_cnt:
            M_cnt = cnt
            
        # 벽 3개 세운 후 필요한 코드실행 모두 끝나면 return해주기
        return
    
    
    # 벽 3개 좌표 고르기
    # start 통해서 조합 구하기(중복 방지)
    for i in range(start, n*m):
        # n*m에서 나올 수 있는 좌표
        row, col = divmod(i, m)
        
        # 0인 곳에 벽을 세워야 하기 때문에 0이 아니면 continue
        if lst[row][col] != 0: continue
        
        # path배열에 벽 세울 좌표 넣어주기
        # level이 2일 때까지 넣어주면 2번 인덱스까지 3개 선택되는 것
        path[level] = [row, col]
        
        # level이 3일 때까지 함수 호출 
        dfs(level+1, i+1)


path = [0]*3
M_cnt = 0
# 함수 실행 
dfs(0, 0)
# 결과 출력 
print(M_cnt)
