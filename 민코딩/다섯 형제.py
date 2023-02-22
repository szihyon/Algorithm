st = list(map(int, input().split()))
cnt = 0
path = [0]*5
used = [0]*len(st)

def abc(level, sum_val):
    global cnt

    if 10 <= sum_val <= 20:
        cnt += 1

    if sum_val > 20:
        return

    if level == 5:
        return

    for i in range(len(st)):
        if level > 0 and path[level-1] > st[i]: continue
        if used[i] == 0:
            path[level] = st[i]
            used[i] = 1
            abc(level+1, sum_val + st[i])
            path[level] = ''
            used[i] = 0

abc(0, 0)
print(cnt)




# 두번째 방법
# #st = list(map(int, input().split()))
# st= [5, 4, 3, 9, 1]
# cnt = 0
#
# def abc(level, sum_val,results=[]):
#     print(level,sum_val,results)
#     global cnt
#     if sum_val>20:
#         return
#     if 10 <= sum_val + st[level] <= 20:
#         cnt += 1
#         print(results+[st[level]])
#
#     if level == 4:
#         return
#
#     abc(level+1, sum_val + st[level], results+[st[level]])
#     abc(level+1, sum_val, results)
#
# abc(0, 0, [])
# print(cnt)
