def solution(cards1, cards2, goal):
    answer = 'Yes'
    for i in range(len(goal)):
        if goal[i] in cards1:
            answer='Yes'
        elif goal[i] in cards2:
            answer='Yes'
        else:
            answer='No'
            break
    return answer