# 방법 1 
# dfs코드 pypy로 돌리기
r, c = map(int, input().split())
lst = [list(input()) for _ in range(r)]

def bfs(stY, stX, cnt, path):
    directY = [-1, 0, 0, 1]
    directX = [0, -1, 1, 0]
    q = set()
    q.add((stY, stX, cnt, path))
    M_cnt = 0

    while q:
        nowY, nowX, cnt, path = q.pop()
        if cnt > M_cnt:
            M_cnt = cnt
        for i in range(4):
            dy = directY[i] + nowY
            dx = directX[i] + nowX
            if dy < 0 or dx < 0 or dy > r-1 or dx > c-1:continue
            if lst[dy][dx] in path: continue
            q.add((dy, dx, cnt+1, path+lst[dy][dx]))

    return M_cnt

path = []
path.append(lst[0][0])
res = bfs(0, 0, 1, lst[0][0])
print(res)



# 방법 2
# set이용해서 bfs처럼 풀기
# r, c = map(int, input().split())
# lst = [list(input()) for _ in range(r)]
# 
# def bfs(stY, stX, cnt, path):
#     directY = [-1, 0, 0, 1]
#     directX = [0, -1, 1, 0]
#     q = set()
#     q.add((stY, stX, cnt, path))
#     M_cnt = 0
# 
#     while q:
#         nowY, nowX, cnt, path = q.pop()
#         if cnt > M_cnt:
#             M_cnt = cnt
#         for i in range(4):
#             dy = directY[i] + nowY
#             dx = directX[i] + nowX
#             if dy < 0 or dx < 0 or dy > r-1 or dx > c-1:continue
#             if lst[dy][dx] in path: continue
#             q.add((dy, dx, cnt+1, path+lst[dy][dx]))
# 
#     return M_cnt
# 
# path = []
# path.append(lst[0][0])
# res = bfs(0, 0, 1, lst[0][0])
# print(res)
