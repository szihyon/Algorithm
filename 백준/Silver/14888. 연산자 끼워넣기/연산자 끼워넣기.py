n = int(input())
nums = list(map(int, input().split()))
ops_inp = list(map(int, input().split()))

ops = ['+', '-', '*', '//']
ops_dict = {ops[i]: ops_inp[i] for i in range(4)}

maxV = -21e8
minV = 21e8

def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '//':
        if a < 0:
            return -((-a) // b)
        return a // b

def dfs(level, result):
    global maxV, minV
    if level == n-1:
        maxV = max(maxV, result)
        minV = min(minV, result)
        return

    for op in ops:
        if ops_dict[op] > 0:
            next_result = calculate(result, nums[level+1], op)
            ops_dict[op] -= 1
            dfs(level+1, next_result)
            ops_dict[op] += 1

dfs(0, nums[0])

print(maxV)
print(minV)