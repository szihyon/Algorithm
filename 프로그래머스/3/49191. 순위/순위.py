def solution(n, results):
    # 승패 정보를 담을 2차원 배열 초기화
    win_lose = [[False] * n for _ in range(n)]
    
    # 경기 결과를 바탕으로 승패 정보 업데이트
    for win, lose in results:
        win_lose[win-1][lose-1] = True
        
    # 플로이드-워셜 알고리즘 적용
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if win_lose[i][k] and win_lose[k][j]:
                    win_lose[i][j] = True
                    
    # 정확한 순위를 매길 수 있는 선수의 수 계산
    answer = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if win_lose[i][j] or win_lose[j][i]:
                count += 1
        if count == n-1:
            answer += 1
            
    return answer