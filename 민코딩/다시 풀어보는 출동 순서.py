lst = ['B', 'I', 'A', 'H']
lst2 = lst[:]
search = 0

n = int(input())

for i in range(3):
    if lst[search] in lst2: # 찾고자 하는 원소가 작업중인 리스트 속에 존재하는지 체크
        start = lst2.index(lst[search]) # 있다면 작업중인 리스트에서 찾고자 하는 원소의 인덱스부터 시작
    else:
        start = lst2.index(lst[search+1])   # 없다면 lst의 다음 원소를 lst2에서 찾고 거기부터 시작
    cnt = 0
    while 1:
        cnt += 1    # 몇 번째인지 세는 변수. 첫번째부터 시작 
        if cnt == n:
            search = lst.index(lst2[start]) + 1 # lst에서 pop한 원소의 다음 인덱스
            print(lst2.pop(start), end=' ') # n번 이동했을 때의 인덱스를 pop
            break
        if start == len(lst2)-1:    # 만약 마지막 인덱스라면, 다시 0번 인덱스로 이동
            start = -1
        start += 1  
print(lst2.pop())   # 남은 하나의 원소 print
