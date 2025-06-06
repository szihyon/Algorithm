import sys
input = sys.stdin.readline

N, M = map(int, input().split())

basket = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    i -= 1
    j -= 1
    for c in range(i, j+1):
        basket[c] = k
        # if basket[c] == 0:
        #     basket[c] = k
        # else:
        #     basket[c] = 0


print(*basket[0:N+1])