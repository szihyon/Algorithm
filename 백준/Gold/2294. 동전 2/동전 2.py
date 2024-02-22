n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

lst = [10001] * (k+1)
lst[0] = 0

for i in range(n):
    for j in range(coins[i], k+1):
        lst[j] = min(lst[j], lst[j-coins[i]]+1)

if lst[k] == 10001:
    print(-1)
else:
    print(lst[k])