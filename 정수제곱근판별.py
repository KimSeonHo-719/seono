import math

def solution(n):
    answer=0
    for i in range(1,round(math.sqrt(n)+1)):
        if n==i**2:
            answer=i
            return (answer+1)**2
    if answer==0:
        return -1
    