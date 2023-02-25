import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    print(f"#{tc}", end = " ")
    bucket = [0] * 5001
    n = int(input())
    for i in range(n):
        st, ed = map(int, input().split())
        for i in range(st, ed+1):
            bucket[i] += 1
    n2 = int(input())
    for i in range(n2):
        print(bucket[int(input())], end=" ")
    print()
