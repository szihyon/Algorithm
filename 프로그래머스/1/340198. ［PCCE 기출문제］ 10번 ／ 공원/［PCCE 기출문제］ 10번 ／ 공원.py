def solution(mats, park):
    answer = -1
    h = len(park)
    w = len(park[0])
    mats.sort(reverse=True) 
    
    def check(mat):
        for i in range(h-mat+1):
            for j in range(w-mat+1):
                flag = True
                for k in range(i, i+mat):
                    for g in range(j, j+mat):
                        if park[k][g] != "-1":
                            flag = False
                            break
                    if not flag:
                        break
                if flag:  
                    return True
        return False
    
    #매트 길이별로 체크
    for mat in mats:
        rlt = check(mat)
        if rlt:
            answer = mat
            break
    
    return answer