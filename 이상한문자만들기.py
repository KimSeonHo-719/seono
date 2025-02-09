def solution(s):
    answer = ''
    cnt=0
    for i in range(len(s)):
        if s[i].isalpha():
            if cnt%2==0:
                answer+=s[i].upper()
            else:
                answer+=s[i].lower()
            cnt+=1
        else:
            answer+=' '
            cnt=0
    return answer