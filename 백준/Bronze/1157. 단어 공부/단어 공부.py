word = input().lower()  # 입력 받은 단어를 소문자로 변환
word_dict = {}

# 알파벳별 사용 빈도 계산
for char in word:
    if char not in word_dict:
        word_dict[char] = 1
    else:
        word_dict[char] += 1

# 사용 빈도를 기준으로 정렬
word_dict2 = sorted(word_dict.items(), key=lambda x:x[1], reverse=True)

# 가장 많이 사용된 알파벳이 여러 개 있는지 확인
if len(word_dict2) > 1 and word_dict2[0][1] == word_dict2[1][1]:
    answer = '?'
else:
    answer = word_dict2[0][0].upper()

print(answer)
