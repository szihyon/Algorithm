# Sum 전역변수로 풀기
T = int(input())

def abc(level):
    global minV, sumV

    if sumV > minV:
        return

    if level == n:
        if sumV < minV:
            minV = sumV
        return

    for i in range(len(factory)):
        if used[i] == 1: continue
        used[i] = 1
        path[level] = factory[i]
        sumV += lst[level][path[level]]
        abc(level+1)
        sumV -= lst[level][path[level]]
        used[i] = 0


for tc in range(1, T+1):
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(list(map(int, input().split())))
    factory = [i for i in range(n)]
    used = [0]*len(factory)
    path = [0]*n
    sumV = 0
    minV = 21e8
    abc(0)
    print(f"#{tc} {minV}")
   
  
#####################################################  
# Sum 매개변수로 풀기
# T = int(input())
#
# def abc(level, sumV):
#     global minV
#
#     if sumV > minV:
#         return
#
#     if level == n:
#         if sumV < minV:
#             minV = sumV
#         return
#
#     for i in range(len(factory)):
#         if used[i] == 1: continue
#         used[i] = 1
#         path[level] = factory[i]
#         abc(level+1, sumV + lst[level][path[level]])
#         used[i] = 0
#
#
# for tc in range(1, T+1):
#     n = int(input())
#     lst = []
#     for i in range(n):
#         lst.append(list(map(int, input().split())))
#     factory = [i for i in range(n)]
#     used = [0]*len(factory)
#     path = [0]*n
#     minV = 21e8
#     abc(0, 0)
#     print(f"#{tc} {minV}")
