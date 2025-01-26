def solution(n):
    answer=0
    for i in range(1, round(n/2)):
        if n%i==1:
            answer=i
            break
    if answer==0:
        answer=n-1
    return answer