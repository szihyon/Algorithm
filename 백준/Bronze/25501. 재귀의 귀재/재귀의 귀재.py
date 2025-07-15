T = int(input())

def recursion(S, start, end):
    if(start >= end): return 1, start+1
    elif S[start] != S[end]: return 0, start+1
    return recursion(S, start+1, end-1)

def isPalindrome(S):
    return recursion(S, 0, len(S)-1)

for t in range(T):
    S = list(input())
    pal, rec = isPalindrome(S)
    print(pal, rec)