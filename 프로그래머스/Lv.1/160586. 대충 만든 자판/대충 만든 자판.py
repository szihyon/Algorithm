def solution(keymap, targets):
    answer = []
    
    def check(target):
        minV = 101
        for i in range(len(keymap)):
            for j in range(len(keymap[i])):
                if keymap[i][j] == target:
                    if j+1 < minV:
                        minV = j+1
                    break
        if minV == 101:
            return -1
        else:
            return minV
    
    for i in range(len(targets)):
        cnt = 0
        for j in range(len(targets[i])):
            if check(targets[i][j]) != -1:
                cnt += check(targets[i][j])
            else:
                cnt = -1
                break
        answer.append(cnt)
    
    return answer