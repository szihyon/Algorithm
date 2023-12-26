def solution(ineq, eq, n, m):
    answer = 0
    if eq == "!":
        eq = ""
    op = ineq + eq
    
    if op == ">":
        if n > m :
            answer = 1
    elif op == "<":
        if n < m :
            answer = 1
    elif op == ">=":
        if n >= m:
            answer = 1
    elif op == "<=":
        if n <= m :
            answer = 1
    
    return answer