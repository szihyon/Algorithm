n = int(input())

for _ in range(n):
    flag = 1
    stack = []
    lst = list(input())
    for i in range(len(lst)):
        if lst[i] == "(":
            stack.append(lst[i])
        else:
            if len(stack) == 0:
                flag = 0
            else:
                stack.pop()
    
    if len(stack) > 0:
        flag = 0

    if flag:
        print("YES")
    else:
        print("NO")
