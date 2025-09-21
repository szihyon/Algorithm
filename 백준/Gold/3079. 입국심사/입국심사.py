N, M = map(int, input().split())
t_lst = []
for _ in range(N):
    t_lst.append(int(input()))

left = 1
right = max(t_lst) * M  #가장 오래걸리는 심사대에만 줄서는 경우 시간
answer = max(t_lst) * M

#이분탐색
while left <= right:
    mid = (left+right)//2
    people = 0
    
    for t in t_lst:
        people += mid//t
    
    if people < M:    #상근이와 친구들 수 보다 적으면
        left = mid+1    #시간 더 늘리기
    else:   #상근이와 친구들 수와 '같거나' 크면
        right = mid-1

answer = left

print(answer)
