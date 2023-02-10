import sys
sys.stdin = open("input.txt", "r")

# N명의 손님들. M초의 시간들이면 K개의 붕어빵.
# 0초 이후 오는 손님들 도착시간

T = int(input())

def func(lst, time, n):
    for i in range(n):
        sumv = sum(lst[:time[i] + 1])
        if sumv != 0:
            for j in range(len(lst)):
                if lst[j] != 0:
                    lst[j] -= 1
                    break
        else:
            return print(f"#{tc} Impossible")
    return print(f"#{tc} Possible")

for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    temp = m
    time = list(map(int, input().split()))
    time.sort()
    lst = [0] * 11112
    while temp < len(lst):
        lst[temp] = k
        temp += m
    func(lst, time, n)




