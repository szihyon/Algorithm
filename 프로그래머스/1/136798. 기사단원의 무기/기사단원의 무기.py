def solution(number, limit, power):
    answer = 0
    lst = [0] * number  # 약수 개수를 저장할 리스트 초기화
    
    # 약수 리스트 만들기
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            lst[j - 1] += 1  # 리스트 인덱스를 0부터 시작하므로 1을 빼줌
        
    # 공격력 제한 체크
    for i in range(len(lst)):
        if lst[i] > limit:
            lst[i] = power
            
    # 공격력 총합
    answer = sum(lst)
    
    return answer