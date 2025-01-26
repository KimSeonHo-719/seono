def solution(n):
    answer = 0
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    n_str=str(n)
    for i in range(0,len(n_str)):
        answer+=int(n_str[i])

    return answer