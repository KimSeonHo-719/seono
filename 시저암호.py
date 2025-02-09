def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].isupper():
                answer+=chr((ord(s[i])-ord('A')+n)%26+ord('A'))
            else:
                answer+=chr((ord(s[i])-ord('a')+n)%26+ord('a'))
        else:
            answer+=s[i]
    return answer