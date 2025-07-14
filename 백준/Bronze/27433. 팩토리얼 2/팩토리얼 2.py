N = int(input())

def fac(num):
    if num == 0:
        return 1
    else:
        return num * fac(num-1)

rlt = fac(N)
print(rlt)