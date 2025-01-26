def solution(arr, divisor):
    answer = []
    sorted_ans=[]
    for i in range(0,len(arr)):
        if arr[i]%divisor==0:
            answer.append(arr[i])
    if not answer:
        return [-1]
    else:
        sorted_ans=sorted(answer)
        return sorted_ans