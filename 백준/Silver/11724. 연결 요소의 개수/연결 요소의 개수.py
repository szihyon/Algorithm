n, m = map(int, input().split())
lst = [[0] * n for _ in range(n)]
for _ in range(m):
    p1, p2 = map(int, input().split())
    lst[p1 - 1][p2 - 1] = 1
    lst[p2 - 1][p1 - 1] = 1

visit = [0] * n


def dfs(now):
    visit[now] = 1  

    for i in range(n):
        if lst[now][i] == 1 and visit[i] == 0:
            dfs(i)  


cnt = 0

for i in range(n):
    if visit[i] == 0:  
        cnt += 1
        dfs(i)

print(cnt)


#####################################################################
# n, m = map(int, input().split())
# lst = [[0]*n for _ in range(n)]
# for _ in range(m):
#     p1, p2 = map(int, input().split())
#     lst[p1-1][p2-1] = 1
#     lst[p2-1][p1-1] = 1
#
# visit = [0]*n
#
# def dfs(now):
#     for i in range(n):
#         if lst[now][i] == 1:
#             if visit[i] == 0:
#                 visit[i] = 1
#                 dfs(i)
#
# cnt = 0
#
# for j in range(n):
#     # 아무 것도 연결되지 않고 혼자 있는 노드는 세지 못하기 때문에 아래 코드 작성하면 안됨
#     # for j in range(n):
#     #     if lst[i][j] == 1:
#
#             if visit[j] == 0:
#                 visit[j] = 1
#                 cnt += 1
#                 dfs(j)
#
# print(cnt)



#############################################################
# 아무 것도 연결되어 있지 않은 노드도 카운트해주기

# n, m = map(int, input().split())
# lst = [[0] * n for _ in range(n)]
# for _ in range(m):
#     p1, p2 = map(int, input().split())
#     lst[p1 - 1][p2 - 1] = 1
#     lst[p2 - 1][p1 - 1] = 1
#
# visit = [0] * n
#
#
# def dfs(now):
#     for i in range(n):
#         if lst[now][i] == 1:
#             if visit[i] == 0:
#                 visit[i] = 1
#                 dfs(i)
#
# cnt = 0
#
# for i in range(n):
#     for j in range(n):
#         if lst[i][j] == 1:
#             if visit[j] == 0:
#                 visit[j] = 1
#                 cnt += 1
#                 dfs(j)
#
# # 아무 것도 연결되어 있지 않는 것들 따로 카운트해주기
# for i in range(n):
#     if visit[i] == 0:
#         cnt += 1
#
# print(cnt)





##############################################################
# 인접 행렬에서 자기 자신도 1 체크해주기

# n, m = map(int, input().split())
# lst = [[0] * n for _ in range(n)]
# for _ in range(m):
#     p1, p2 = map(int, input().split())
#     lst[p1 - 1][p2 - 1] = 1
#     lst[p2 - 1][p1 - 1] = 1
#
# visit = [0] * n
#
# # 자기 자신도 연결 체크
# for i in range(n):
#     lst[i][i] = 1
#
# def dfs(now):
#     for i in range(n):
#         if lst[now][i] == 1:
#             if visit[i] == 0:
#                 visit[i] = 1
#                 dfs(i)
#
# cnt = 0
#
# for i in range(n):
#     for j in range(n):
#         if lst[i][j] == 1:
#             if visit[j] == 0:
#                 visit[j] = 1
#                 cnt += 1
#                 dfs(j)
#
# print(cnt)
