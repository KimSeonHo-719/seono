def solution(arr):
    answer = arr
    sort=sorted(arr)
    if len(sort)==1:
        answer.pop()
        answer.append(-1)
    else:
        small=sort[0]
        for i in range(len(answer)):
            if answer[i]==small:
                answer.pop(i)
                break
    return answer