def solution(cards1, cards2, goal):
    answer = 'Yes'
    j,k=0,0
    for word in goal:
        if j<len(cards1) and word==cards1[j]:
            j+=1
        elif k<len(cards2) and word==cards2[k]:
            k+=1
        else:
            answer='No'
            break
    return answer