import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
broken = list(input().split())

min_count = abs(100 - N)

for num in range(1000000):
    num = str(num)
    for i in range(len(num)):
        if num[i] in broken:
            break
        elif i == len(num)-1:
            min_count = min(min_count, abs(N-int(num))+len(num))

print(min_count)