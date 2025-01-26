def solution(x):
    answer = True
    str_x=str(x)
    sum=0
    for i in range(0,len(str_x)):
        sum+=int(str_x[i])
    if x%sum==0:
        return answer
    else:
        return False