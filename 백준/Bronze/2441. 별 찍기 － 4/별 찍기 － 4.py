import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    temp = [' ']*N
    # for j in range(N, N-i-1, -1):
    for j in range(i, N):
        # print(j, end='')
        temp[j] = '*'
    print(''.join(temp))