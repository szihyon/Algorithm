lst = []

for _ in range(4):
    lst.append(list(input()))

dir = 0

def Move(lst):
    global dir
    monster = ['A', 'C', 'D']
    directionY = [0, 1, 0, -1]
    directionX = [1, 0, -1, 0]
    for i in range(3):
        target = monster[i]
        flag = 0
        for j in range(4):
            for k in range(3):
                if lst[j][k] == target:
                    flag = 1
                    if (directionY[dir] + j) < 0 or (directionX[dir] + k) < 0 or (directionY[dir] + j) > 3 or (directionX[dir] + k) > 2: break
                    if lst[directionY[dir] + j][directionX[dir] + k] == "#": break
                    if lst[directionY[dir] + j][directionX[dir] + k].isalpha(): break
                    lst[directionY[dir] + j][directionX[dir] + k] = target
                    lst[j][k] = '_'
                    break
            if flag == 1:
                break
    dir = (dir % 3)
    return lst


for _ in range(5):
    Move(lst)


for i in lst:
    print(*i, sep='')
