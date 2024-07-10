nums = []
for _ in range(9):
    nums.append(list(map(int, input())))

# 숫자를 채워야하는 곳들 저장
empty = []
for i in range(9):
    for j in range(9):
        if nums[i][j] == 0:
            empty.append([i, j])

# 중복 숫자 체크 (행, 열, 3x3영역)
def check(num, y, x):
    for c in range(9):
        if nums[y][c] == num: return False # 행 체크
        if nums[c][x] == num: return False # 열 체크
    # 3x3영역 체크
    y = (y//3)*3
    x = (x//3)*3
    for i in range(3):
        for j in range(3):
            if nums[y+i][x+j] == num: return False
    return True

n = len(empty)
flag = 0
def dfs(level):
    global flag
    if flag == 1: # 이미 정답을 찾은 경우 더 이상 진행X
        return

    if level == n: # 빈 공간을 모두 채웠다면 체크 후 출력 
        flag = 1
        for k in range(len(nums)):
            for g in range(len(nums[k])):
                print(nums[k][g], end='')
            print()
        return
    
    # 빈칸에 숫자 1~9까지 넣어보고 중복체크
    y, x = empty[level]
    for num in range(1, 10):
        if check(num, y, x):
            nums[y][x] = num
            dfs(level+1)
            nums[y][x] = 0

# dfs 함수 실행 
dfs(0)