def solution(name, yearning, photo):
    answer = []
    dict={}
    for i in range(len(name)):
        dict[name[i]]=yearning[i]
    for i in range(len(photo)):
        sum=0
        for j in range(len(photo[i])):
            if photo[i][j] in dict:
                sum+=dict[photo[i][j]]
        answer.append(sum)
        
    return answer