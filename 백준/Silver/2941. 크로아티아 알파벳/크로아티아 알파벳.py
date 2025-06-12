S = input()
alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for a in alphabet:
    S = S.replace(a, '*')  

print(len(S))
