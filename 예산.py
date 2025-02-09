def solution(d, budget):
    answer = 0
    sum=0
    sort=sorted(d)
    for i in range(len(sort)):
        if budget>=sum+sort[i]:
            sum+=sort[i]
            answer+=1
    return answer