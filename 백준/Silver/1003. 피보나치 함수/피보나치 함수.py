T = int(input())
memo = [[] for _ in range(41)]
memo[1] = [0, 1]
memo[0] = [1, 0]

def fibonacci(num):
    global memo
    if num >= 2 and not memo[num]:
        memo[num] = [fibonacci(num-1)[0] + fibonacci(num-2)[0], fibonacci(num-1)[1] + fibonacci(num-2)[1]]
    return memo[num]

for _ in range(T):
    num = int(input())
    zero, one = fibonacci(num)
    print(zero, one)