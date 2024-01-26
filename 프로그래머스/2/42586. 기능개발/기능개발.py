def solution(progresses, speeds):
    answer = []
    while progresses:
        if progresses[0] < 100:
            for i in range(len(progresses)):
                if progresses[i] < 100:
                    progresses[i] = progresses[i] + speeds[i]
        cnt = 0
        while progresses and progresses[0] >= 100:
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)
        if cnt != 0 :
            answer.append(cnt)
        
    return answer