def solution(A, B):
    answer = 0
    if A == B:
        return answer
    for i in range(len(A)):
        new_str = ""
        new_str += A[-1]
        answer += 1
        for i in range(len(A)-1):
            new_str += A[i]
        if new_str == B:
            return answer
        A = new_str
    return -1