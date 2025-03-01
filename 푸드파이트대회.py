def solution(food):
    answer = ''
    string=''
    for i in range(1, len(food)):
        for j in range(food[i]//2):
            string+=str(i)
    sorted_string=string[::-1]
    answer=string+'0'+sorted_string
    return answer