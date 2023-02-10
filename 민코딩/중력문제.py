lst = []
new_lst = [[],[],[]]

for i in range(4):
    lst.append(list(input()))

for i in range(3):
    for j in range(4):
        if lst[j][i] != "_":
            new_lst[i].append(lst[j][i])

for i in new_lst:
    while len(i) < 4:
        i.insert(0, "_")

for i in range(4):
    for j in range(3):
        print(new_lst[j][i], end="")
    print()
