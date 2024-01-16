def solution(s, skip, index):
    answer = ''
    for alphabet in s:
        i = 1
        cnt = 0
        while cnt < index:
            check_alphabet = ord(alphabet) + i
            if check_alphabet > ord('z'):
                while check_alphabet > ord('z') or check_alphabet < ord('a'):
                    check_alphabet -= ord('z') - ord('a') + 1
            if chr(check_alphabet) not in skip:
                cnt += 1
            i += 1
        answer += chr(check_alphabet)
    return answer