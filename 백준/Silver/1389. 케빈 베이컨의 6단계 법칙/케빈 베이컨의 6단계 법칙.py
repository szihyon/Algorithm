from collections import deque

N, M = map(int, input().split())
lst = [[] for _ in range(N+1)]

for _ in range(M): #친구관계 입력
    A, B = map(int, input().split())
    lst[A].append(B)
    lst[B].append(A)

# def dfs(now, end, cnt):
#     if now == end:
#         temp.append(cnt)
#         return
#     for next in lst[now]:
#         if visit[next] == 1: continue
#         visit[next] = 1
#         dfs(next, end, cnt+1)
#         visit[next] = 0

def bfs(start, end):
    temp = []
    q = deque()
    for n in lst[start]:
        q.append([n, 0])
    visit = [0] * (N + 1)
    visit[start] = 1

    while q:
        now, cnt = q.popleft()
        if now == end:
            return cnt
        for next in lst[now]:
            if visit[next] == 1: continue
            visit[next] = 1
            q.append([next, cnt+1])

    return False


answer_lst = []
for start in range(1, N+1): # 시작 지점
    temp_cnt = 0
    for end in range(1, N+1): # 끝 지점
        if start == end: continue
        res = bfs(start, end)
        temp_cnt += res
    answer_lst.append([start, temp_cnt])

answer_lst = sorted(answer_lst, key=lambda x:(x[1], x[0]))
print(answer_lst[0][0])