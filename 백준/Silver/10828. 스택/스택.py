import sys
stack = []

for i in range(int(sys.stdin.readline())):
    lst = sys.stdin.readline().split()
    if lst[0] == 'push':
        stack.append(lst[1])
    if lst[0] == 'pop':
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    if lst[0] == 'size':
        print(len(stack))
    if lst[0] == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
    if lst[0] == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)