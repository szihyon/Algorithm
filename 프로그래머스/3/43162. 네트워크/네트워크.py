from collections import deque

def solution(n, computers):
    answer = 0
    used = [0]*n
    
    def bfs(start):
        q = deque()
        used[start] = 1
        q.append(start)
        while q:
            now = q.popleft()
            for i in range(n):
                if computers[now][i] == 1 and used[i] == 0:
                    used[i] = 1
                    q.append(i)
        return
    
    for i in range(n):
        if used[i] == 0:
            answer += 1
            bfs(i)
            
    return answer