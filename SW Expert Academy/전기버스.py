import sys
sys.stdin = open("input.txt", "r")

T = int(input())
 
for tc in range(1, T + 1):
    k, n, m = map(int, input().split())
    c = list(map(int, input().split()))
    cnt = 0
    flag = 1
    last_charge = 0
 
    if c[-1] != n:
        c = c + [n]
 
    for i in range(len(c) - 1):
        if c[i] + k < c[i + 1]:
            flag = 0
 
    if flag:
        for i in range(len(c)-1):
            if last_charge + k < c[i+1]:
                last_charge = c[i]
                cnt += 1
 
    print(f"#{tc} {cnt}")
