def solution(s):
    answer = True
    for i in range(len(s)):
        if s[i].isalpha():
            answer=False
        if len(s)!=4 and len(s)!=6:
            answer=False
    return answer