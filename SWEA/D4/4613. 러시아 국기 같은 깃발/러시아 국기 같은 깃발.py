def Count(bluestart, redstart):
    rt = 0
    for i in range(len(lst)):
        if i < bluestart:
            rt += M - lst[i].count("W")
        elif i < redstart:
            rt += M - lst[i].count("B")
        else:
            rt += M - lst[i].count("R")
    return rt


TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    lst = []
    for _ in range(N):
        lst.append(input())
    mincount = N * M
    for bluestart in range(1, N):
        for redstart in range(bluestart + 1, N):
            thiscount = Count(bluestart, redstart)
            if thiscount < mincount:
                mincount = thiscount
    print("#{} {}".format(tc, mincount))