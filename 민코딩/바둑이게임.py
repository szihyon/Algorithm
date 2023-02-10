# https://pro.mincoding.co.kr/problem-step/3/level/42/detail/G3LV21_5_%EB%B0%94%EB%91%91%EC%9D%B4%EA%B2%8C%EC%9E%84

# lst = [[0,0,0,0,0,0,0],[0,0,1,0,1,0,0],[0,1,2,0,2,1,0],[0,0,1,2,1,0,0],[0,0,2,1,0,1,0],[0,1,1,0,0,0,0],[0,0,0,0,0,0,0]]
# directY = [-1, 0, 0, 1]
# directX = [0, -1, 1, 0]
# w1, w2 = map(int, input().split())
# lst[w1][w2] = 1
#
# def check(y, x):
#     res = 0
#     for i in range(4):
#         dy = directY[i] + y
#         dx = directX[i] + x
#         if dy < 0 or dx < 0 or dy > 6 or dx > 6:
#             continue
#         if lst[dy][dx] == 1:
#             res += 1
#     if res == 4:
#         return True
#
# cnt = 0
# for i in range(len(lst)):
#     for j in range(len(lst[i])):
#         if lst[i][j] == 2:
#             if check(i, j):
#                 cnt += 1
#
# print(cnt)