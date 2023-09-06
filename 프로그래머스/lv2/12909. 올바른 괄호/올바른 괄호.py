def solution(s):
    answer = True
    n = len(s)
    stack = []
    for i in range(n):
        if s[i] == "(":
            stack.append(s[i])
        if s[i] == ")":
            if stack:
                stack.pop()
            else:
                return False
    if len(stack) > 0:
        return False
    return True