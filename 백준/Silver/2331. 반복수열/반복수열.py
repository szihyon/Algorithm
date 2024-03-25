A, P = map(int, input().split())
num_list = []
stop_N = 0
def dfs(num):
    global stop_N
    num = list(str(num))
    sumV = 0
    for n in num:
        sumV += int(n)**P
    if sumV in num_list:
        stop_N = sumV
        return
    else:
        num_list.append(sumV)
        dfs(sumV)

num_list.append(A)
dfs(A)

idx = num_list.index(stop_N)
print(idx)