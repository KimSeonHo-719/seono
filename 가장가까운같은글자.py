def solution(s):
    answer = []
    for i in range(len(s)):
        for j in range(0,i-1):
            if s[i]==s[j]:
                answer.append(j)
    return answer