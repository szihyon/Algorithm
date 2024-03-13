from collections import deque
def solution(n, edge):

    answer = 0
    lst = [[] for _ in range(n+1)]
    for i in range(len(edge)):
        lst[edge[i][0]].append(edge[i][1])
        lst[edge[i][1]].append(edge[i][0])
    
    def bfs(start):
        q = deque()
        q.append([start, 0])
        while q:
            now, distance = q.popleft()
            distance_lst[now] = distance
            for next in lst[now]:
                if used[next] == 1: continue
                used[next] = 1
                q.append([next, distance+1])
        return
    
    distance_lst = [0]*(n+1)
    used = [0]*(n+1)
    bfs(1)
    distance_lst[1] = 0 

    maxV = max(distance_lst)
    for i in range(len(distance_lst)):
        if distance_lst[i] == maxV:
            answer += 1
    
    return answer