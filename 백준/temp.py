x, y = map(int, input().split())

mint=None
def DFS(X,Y,t):
    global mint
    if t>mint:
        return
    if X==Y:
        mint=t
        return
    DFS(X+1,Y,t+1)
    DFS(X-1,Y,t+1)
    DFS(2*X,Y,t+1)

def find(X,Y):
    global mint
    mint=abs(X-Y)
    DFS(X,Y,0)
    return mint

print(find(x,y))

######################
x, y = map(int, input().split())

def find(X,Y):
    loc={X}
    for t in range(0,100):
        print(t,loc)
        if Y in loc:
            break
        newloc={x-1 for x in loc}
        newloc.update({x+1 for x in loc})
        newloc.update({2*x for x in loc})
        loc=newloc
    return t

print(find(x,y))
