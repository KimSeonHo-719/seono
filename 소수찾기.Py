import math

def solution(n):
    answer = n-2
    for i in range(2,n):
        float j=math.sqrt(i)
        if i==j**2:
            answer-=1
    return answer