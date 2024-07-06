from collections import deque

N = int(input())
nums = [[] for _ in range(N+1)]
for i in range(1, N+1):
    nums[i].append(int(input()))

def bfs(start):
    q = deque()
    q.append(start)
    used = [0]*(N+1)
    used[start] = 1

    while q:
        now = q.popleft()
        for next in nums[now]:
            if next == start:
                return True
            if used[next] == 1: continue
            used[next] = 1
            q.append(next)
    return False

ans_cnt = 0
ans_lst = []
for i in range(1, N+1):
    res = bfs(i)
    if res:
        ans_cnt += res
        ans_lst.append(i)

print(ans_cnt)
for ans in ans_lst:
    print(ans)