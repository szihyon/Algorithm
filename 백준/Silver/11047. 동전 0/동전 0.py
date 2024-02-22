N, K = map(int, input().split())
coins = []

for i in range(N):
    coins.append(int(input()))

cnt = 0
for i in range(N-1, -1, -1):
    if K == 0:
        break
    cnt += K // coins[i]
    K = K % coins[i]

print(cnt)