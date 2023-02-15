lst = [3, 4, 1, 5, 2, 6]

arr = [
    [0,0,0,1,0,0],
    [0,0,1,0,0,0],
    [1,0,0,1,0,1],
    [0,0,1,0,0,0],
    [0,1,1,0,0,0],
    [0,0,0,0,0,0]
]

visit = [0]*6
a, b = map(int, input().split())

for i in range(len(lst)):
    if lst[i] == a:
        idx1 = i
    if lst[i] == b:
        idx2 = i

Min = 21e8
flag = 0
def abc(now, sum):
    global Min, flag
    if now == idx2:
        flag = 1
        if sum < Min:
            Min = sum

    for i in range(6):
        if arr[now][i] == 1:
            if visit[i] == 0:
                visit[i]=1
                abc(i, sum+1)
                visit[i]=0

visit[idx1] = 1
abc(idx1, 0)
if flag == 1:
    print(Min)
else:
    print(0)
