def solution(s):
    answer = ''
    for i in range(len(s)):
        s[i]=chr(ord(s[i])+1)
        
    return answer