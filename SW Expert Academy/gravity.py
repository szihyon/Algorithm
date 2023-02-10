import sys
sys.stdin = open("input2.txt", "r")

tc = int(input())

for i in range(tc):
    n = int(input())
    nums = list(map(int, input().split()))
    drop = [0]*n
    cnt = 0
    for j in range(n):
        for k in range(j+1, n):
            if nums[j] > nums[k]:
                cnt += 1
        drop[j] = cnt
        cnt = 0
    drop = sorted(drop, reverse=True)
    print(f"#{i+1} {drop[0]}")