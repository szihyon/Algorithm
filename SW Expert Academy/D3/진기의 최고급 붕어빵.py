# 누적합 리스트 전체 -1
T = int(input())

for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    customer = list(map(int, input().split()))
    customer = sorted(customer)
    lst = [0]*(customer[-1]+1)
    # 초를 인덱스로 붕어빵 개수 저장
    for i in range(1, len(lst)):
        if i % m == 0:
            lst[i] = k
    # 누적합 만들기
    for i in range(1, len(lst)):
        lst[i] = lst[i-1] + lst[i]

    flag = 1
    for i in range(len(customer)):
        if lst[customer[i]] >= 1:
            lst = list(map(lambda x:x-1, lst))
        else:
            flag = 0
            break

    if flag:
        print(f"#{tc} Possible")
    else:
        print(f"#{tc} Impossible")
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 1인 수를 발견하면 -1로 바꾸기
# import sys
# sys.stdin = open("input.txt", "r")

# T = int(input())

# def func(lst, time, n):
#     for i in range(n):
#         sumv = sum(lst[:time[i] + 1])
#         if sumv != 0:
#             for j in range(len(lst)):
#                 if lst[j] != 0:
#                     lst[j] -= 1
#                     break
#         else:
#             return print(f"#{tc} Impossible")
#     return print(f"#{tc} Possible")

# for tc in range(1, T+1):
#     n, m, k = map(int, input().split())
#     temp = m
#     time = list(map(int, input().split()))
#     time.sort()
#     lst = [0] * 11112
#     while temp < len(lst):
#         lst[temp] = k
#         temp += m
#     func(lst, time, n)




