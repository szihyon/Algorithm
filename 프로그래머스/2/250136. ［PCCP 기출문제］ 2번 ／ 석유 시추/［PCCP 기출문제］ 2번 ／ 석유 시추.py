from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    
    # 석유 덩어리 정보를 저장
    oil_group = [[0] * m for _ in range(n)]  # 각 칸이 속한 덩어리 번호
    oil_size = {}  # 각 덩어리의 크기
    group_id = 1
    
    # BFS로 석유 덩어리 찾기
    def bfs(start_y, start_x, group_id):
        queue = deque([(start_y, start_x)])
        oil_group[start_y][start_x] = group_id
        size = 1
        
        directY = [-1, 1, 0, 0]
        directX = [0, 0, -1, 1]
        
        while queue:
            y, x = queue.popleft()
            
            for d in range(4):
                dy = y + directY[d]
                dx = x + directX[d]
                
                # 범위 체크
                if dy < 0 or dx < 0 or dy >= n or dx >= m:
                    continue
                    
                # 석유가 있고 아직 방문하지 않은 곳
                if land[dy][dx] == 1 and oil_group[dy][dx] == 0:
                    oil_group[dy][dx] = group_id
                    size += 1
                    queue.append((dy, dx))
        
        return size
    
    # 1단계: 모든 석유 덩어리 찾기
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and oil_group[i][j] == 0:
                oil_size[group_id] = bfs(i, j, group_id)
                group_id += 1
    
    # 2단계: 각 열에서 얻을 수 있는 석유량 계산
    max_oil = 0
    for col in range(m):
        # 이 열에서 만나는 석유 덩어리들
        groups_in_col = set()
        
        for row in range(n):
            if oil_group[row][col] > 0:
                groups_in_col.add(oil_group[row][col])
        
        # 이 열에서 얻을 수 있는 총 석유량
        total_oil = sum(oil_size[g] for g in groups_in_col)
        max_oil = max(max_oil, total_oil)
    
    return max_oil