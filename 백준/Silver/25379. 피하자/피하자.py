N = int(input())
arr = list(map(int, input().split()))

cnt_odd_left = 0
cnt = 0
for a in arr:
    if a % 2 == 1:
        cnt += 1
    else:
        cnt_odd_left += cnt 

cnt_even_left = 0
cnt = 0
for a in arr:
    if a % 2 == 0:
        cnt += 1
    else:
        cnt_even_left += cnt 


print(min(cnt_odd_left, cnt_even_left))