def solution(n):
    str_n = str(n)
    sorted_n=sorted(str_n)
    answer = 0
    for i in range(0,len(sorted_n)):
        answer+=int(sorted_n[i])*(10**i)
    return answer