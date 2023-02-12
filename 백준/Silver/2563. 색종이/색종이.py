n = int(input())
arr = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1

ans = 0
for i in arr:
    ans += i.count(1)
print(ans)
