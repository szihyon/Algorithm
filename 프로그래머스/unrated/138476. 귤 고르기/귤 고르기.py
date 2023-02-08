def solution(k, tangerine):
    counts={}
    for t in tangerine:
        if t in counts:
            counts[t]+=1
        else:
            counts[t]=1
    lst=sorted(counts.items(),key=lambda x:x[1],reverse=True)
    x=0
    for i in range(len(lst)):
        x+=lst[i][1]
        if x>=k:
            break
    return i+1