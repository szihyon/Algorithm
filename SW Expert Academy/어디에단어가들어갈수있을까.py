import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def hor(lst, n, k):
    total = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if lst[i][j] == 1:
                cnt += 1
            else:
                if cnt == k:
                    total += 1
                cnt = 0
        if cnt == k:
            total += 1

    return total

def ver(lst, n, k):
    total = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if lst[j][i] == 1:
                cnt += 1
            else:
                if cnt == k:
                    total += 1
                cnt = 0
        if cnt == k:
            total += 1

    return total

for tc in range(1, T+1):
    n, k = map(int, input().split())
    lst = []
    for i in range(n):
        lst.append(list(map(int, input().split())))
    ans = hor(lst, n, k) + ver(lst, n, k)
    print(f"#{tc} {ans}")
