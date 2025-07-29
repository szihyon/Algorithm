# 입력값
board = []
for _ in range(5):
    board.append(list(map(int, input().split())))
startY, startX = map(int, input().split())

answer = 0
def dfs(y, x, move, apple):
    global answer
    if move > 3:
        return
    if apple >= 2:
        answer = 1
    directY = [-1, 1, 0, 0]
    directX = [0, 0, -1, 1]
    for i in range(4):
        dy = directY[i] + y
        dx = directX[i] + x
        if dy<0 or dx<0 or dy>4 or dx>4: continue
        if board[dy][dx] == -1: continue
        if board[dy][dx] == 1: #사과가 있으면 
            board[dy][dx] = -1
            dfs(dy, dx, move+1, apple+1)
            board[dy][dx] = 1
        else: #사과가 없으면
            board[dy][dx] = -1
            dfs(dy, dx, move+1, apple)
            board[dy][dx] = 0

# 시작점 
if board[startY][startX] == 1:
    board[startY][startX] = -1 
    dfs(startY, startX, 0, 1)
if board[startY][startX] != -1:
    board[startY][startX] = -1 
    dfs(startY, startX, 0, 0)

if answer: 
    print(1)
else:
    print(0)