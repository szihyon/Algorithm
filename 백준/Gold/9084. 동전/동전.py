T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    dp = [0]*(M+1)
    dp[0] = 1
    for coin in coins:
        for money in range(coin, M+1):
            dp[money] = dp[money-coin] + dp[money]
    print(dp[M])