lst = ["A", "B", "C", "D"]
path = [""]*3
result = []
search = input()

def abc(level):
    global temp
    if level == 3:
        temp = ''
        for i in range(len(path)):
            temp += path[i]
        result.append(temp)
        return

    for i in range(4):
        path[level] = lst[i]
        abc(level+1)

abc(0)

for i in range(len(result)):
    if result[i] == search:
        print(f"{i+1}번째")
        break