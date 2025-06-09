N = int(input())

for i in range(N, -1, -1):
    space = ' ' * (N-i)
    star = '*' * (2*i-1)
    print(space + star)