def solution(n, q, ans):
    answer = 0
    code_lst = []
    used_code = [0]*(n+1)   #중복체크
    
    #비밀코드: 1부터 n까지 서로 다른 정수 5개 오름차순
    def code_comb(n, codes, level):
        if level == 5:
            code_lst.append(codes)
            return
        for code in range(1, n+1):
            if level>=1: 
                if codes[-1] > code: continue   #이전 숫자보다 커야함(오름차순)
            if used_code[code] == 1: continue   #이미 사용한 숫자는 패스
            used_code[code] = 1 #사용 체크
            code_comb(n, codes+[code], level+1)
            used_code[code] = 0 #백트래킹 
    
    #가능한 비밀코드 조합 리스트 구하기
    code_comb(n, [], 0)
    
    #m번의 시도 = len(ans)
    m = len(ans)
    #q: 서로 다른 5개의 정수 입력값
    #가능한 비밀코드들과 입력값들(q) 공통 숫자가 ans로 출력되는지 확인 (answer+1)
    for c in range(len(code_lst)):
        temp = []
        for i in range(m):
            cnt = 0
            for j in range(5):
                if q[i][j] in code_lst[c]:
                    cnt += 1
            temp.append(cnt)
        if temp == ans:
            answer += 1

    return answer


    
    
    
    
    