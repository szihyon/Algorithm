def solution(tickets):
    answer = []
    n = len(tickets)
    ans_lst = []
    
    # 경로를 탐색하는 DFS 함수
    def dfs(now, path):
        if len(path) == n+1:
            ans_lst.append(path)
            return
        
        for i in range(len(tickets)):
            if tickets[i][0] == now and visit[i] == 0:
                visit[i] = 1
                dfs(tickets[i][1], path+[tickets[i][1]])
                visit[i] = 0
    
    # ICN이 출발지인 곳에서 DFS 함수 실행
    for i in range(n):
        if tickets[i][0] == "ICN":
            start = i
            visit = [0]*n
            visit[start] = 1
            path = [tickets[start][0], tickets[start][1]]
            dfs(tickets[start][1], path)
    
    # 가능한 루트들 알파벳 순으로 정렬하기
    sorted_routes = sorted(ans_lst, key=lambda x: x)
    answer = sorted_routes[0]

    return answer