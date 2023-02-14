lst=list(map(int,input().split()))
a=1
b=len(lst)-1
while a<b:
    while lst[a]<lst[0]:
        a+=1
    while lst[b]>lst[0]:
        b-=1
    if a>b:
        lst[b],lst[0]=lst[0],lst[b]
    else:
        lst[a],lst[b]=lst[b],lst[a]

print(lst)