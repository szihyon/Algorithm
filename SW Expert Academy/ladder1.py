import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):
    n = int(input())
    lst = []
    for _ in range(100):
        nums = [0] + list(map(int, input().split())) + [0]
        lst.append(nums)
    for i in range(102):
        if lst[99][i] == 2:
            y = i
    x = 99
    while x > 0:
        lst[x][y] = "P"
        if lst[x][y+1] == 1:
            y = y+1
        elif lst[x][y-1] == 1:
            y = y-1
        elif lst[x-1][y] == 1:
            x = x-1
    ans = y-1
    print(f"#{n} {ans}")

