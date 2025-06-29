def solution(schedules, timelogs, startday):
    n = len(schedules)
    answer=n
    for i in range(len(schedules)):
        if schedules[i]%100+10>=60:
            limit=(schedules[i]//100+1)*100+(schedules[i]%100+10)%60
        else:
            limit=schedules[i]+10
        if limit >= 2400:
            limit -= 2400
        for j in range(7):
            actual_day = (startday + j-1) % 7
            if actual_day>=5:
                continue
            if timelogs[i][j] > limit:
                answer -= 1
                break
        
    return answer