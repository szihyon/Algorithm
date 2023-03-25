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
