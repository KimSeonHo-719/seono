def solution(k, score):
    answer = []
    real_score=[]
    for i in range(k):
        answer[i].append(score[i])
        answer.sort(reverse=True)
        real_score.append(answer[i])
    for i in range(k,len(score)):
        if score[i]>answer[k-1]:
            answer.append(score[i])
            answer.sort()
            real_score.append(answer[i])
    return real_score