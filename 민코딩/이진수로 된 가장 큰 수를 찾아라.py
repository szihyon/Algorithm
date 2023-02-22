lst = []

# 3개의 문자열 
for i in range(3):
    lst.append(list(input()))

maxV = 0

# 길이가 더 길면 더 큰 수 
for i in range(len(lst)-1):
    if len(lst[i]) == len(lst[i+1]):    # 길이가 같으면 
        for j in range(len(lst[i])):
            if lst[i][j] == '0' and lst[i+1][j] == '1': # 먼저 0이 나오는 수가 더 작은 수 
                maxV = lst[i+1]
                break
            elif lst[i+1][j] == '0' and lst[i][j] == '1':
                maxV = lst[i]
                lst[i], lst[i+1] = lst[i+1], lst[i] # 더 큰 수가 뒤쪽에 위치해야한다는 점 주의!!
                break
    elif len(lst[i]) > len(lst[i+1]):
        maxV = lst[i]
    else:
        maxV = lst[i+1]

print(*maxV, sep='')
