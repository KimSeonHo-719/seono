def solution(k, score):
    answer = []
    singer=[]
    for i in range(len(score)):
        singer.append(score[i])
        singer.sort(reverse=True)
        if len(singer)<k:
            answer.append(singer[len(singer)-1])
        else:
            answer.append(singer[k-1])
    return answer