import heapq
def solution(operations):
    answer = []
    for operation in operations:
        op, num = operation.split()
        num = int(num)
        if op == 'I':
            heapq.heappush(answer, num)
        else:
            if num == 1:
                if answer:
                    answer.pop(-1)
            else:
                if answer:
                    answer.pop(0)
    if len(answer) == 0:
        answer = [0, 0]
    else:
        answer = [max(answer), min(answer)]
    return answer