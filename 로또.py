def solution(lottos, win_nums):
    answer = []
    max,min=0,0
    for num in lottos:
        if num==0:
            max+=1
        else:
            for num2 in win_nums:
                if num==num2:
                    max+=1
                    min+=1
                    break
    if min==0:
        answer.append(7-max)
        answer.append(6)
    elif max==0:
        answer.append(6)
        answer.append(6)
    else:
        answer.append(7-max)
        answer.append(7-min)
    return answer