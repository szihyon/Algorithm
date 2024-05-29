word = input()

alpha = [chr(i) for i in range(97, 123)]
for a in alpha:
    print(word.count(a), end=' ')