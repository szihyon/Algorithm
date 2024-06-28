N = int(input())

check = '369'
rst = 0

for i in range(1, N+1):
    str_num = str(i)
    for c in check:
        rst += str_num.count(c)

print(rst)