def inorder(i):
    if i:
        inorder(left[i])
        print(str[i], end='')
        inorder(right[i])
    return

for tc in range(1, 11):
    n = int(input())
    lst = [''] * (n + 1)
    left = [''] * (n + 1)
    right = [''] * (n + 1)
    str = [''] * (n + 1)
    for i in range(n):
        inp = input().split()
        if len(inp) == 4:
            left[int(inp[0])] = int(inp[2])
            right[int(inp[0])] = int(inp[3])
            str[int(inp[0])] = inp[1]
        elif len(inp) == 3:
            left[int(inp[0])] = int(inp[2])
            str[int(inp[0])] = inp[1]
        elif len(inp) == 2:
            str[int(inp[0])] = inp[1]

    print(f"#{tc}", end=' ')
    inorder(1)
    print()

    
    
##############################
# 리스트 여러개 만들지 않고 풀이 
T = 10
for test_case in range(1, T + 1):
    n=int(input())
    arr=[[] for _ in range(n+1)]
     
    for i in range(n):
        instr=input().split()
        arr[int(instr[0])].append(instr[1])             #문자
        if len(instr)>2:
            arr[int(instr[0])].append(instr[2])         #왼쪽 자식 노드
        if len(instr)>3:
            arr[int(instr[0])].append(instr[3])         #오른쪽 자식 노드
 
    def func(node):
        if len(arr[node])>1:                 #왼쪽 자식 있으면 먼저 방문
            func(int(arr[node][1]))
 
        print(arr[node][0],end='')              #문자 출력
         
        if len(arr[node])>2:                 #오른쪽 자식 있으면 방문
            func(int(arr[node][2]))
 
    print(f'#{test_case}',end=' ')
    func(1)
    print()
