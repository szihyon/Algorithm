# lst[1:5] = lst[4:0:-1]

n, m = map(int, input().split())
lst = [i+1 for i in range(n)]

for i in range(m):
    i, j = map(int, input().split())
    i -= 1 # 0
    j -= 1 # 3
    k = i-1
    if k == -1:
        lst[i:j+1] = lst[j::-1]
        continue
    lst[i:j+1] = lst[j:k:-1]

print(*lst) 