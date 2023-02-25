import sys
sys.stdin = open("input.txt", "r")

def get_max(lst):
    maxv = lst[0]
    maxidx = 0
    for j in range(len(lst)):
        if lst[j] > maxv:
            maxv = lst[j]
            maxidx = j
    return maxidx

def get_min(lst):
    minv = lst[0]
    minidx = 0
    for k in range(len(lst)):
        if lst[k] < minv:
            minv = lst[k]
            minidx = k
    return minidx

for tc in range(1, 11):
    dump = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    ans = 0
    for i in range(dump):
        if lst[get_max(lst)] - lst[get_min(lst)] <= 1:
            break
        lst[get_max(lst)] = lst[get_max(lst)]-1
        lst[get_min(lst)] = lst[get_min(lst)]+1
    ans = lst[get_max(lst)] - lst[get_min(lst)]
    print(f"#{tc} {ans}")




