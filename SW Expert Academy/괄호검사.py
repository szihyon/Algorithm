def check(ss):
    lst=[]
    for s in ss:
        if s in ["{","("]:
            lst.append(s)
        elif s=="}":
            if len(lst) > 0:
                if lst.pop()!="{":
                    return 0
            else:
                return 0
        elif s==")":
            if len(lst) > 0:
                if lst.pop()!="(":
                    return 0
            else:
                return 0
    if len(lst):
        return 0
    return 1

TC=int(input())
for tc in range(1,TC+1):
    ss=input()
    print(f"#{tc} {check(ss)}")
