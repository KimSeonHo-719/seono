def solution(answers):
    answer = []
    soo1=[1,2,3,4,5]
    soo2=[2,1,2,3,2,4,2,5]
    soo3=[3,3,1,1,2,2,4,4,5,5]
    cnt1,cnt2,cnt3=0,0,0
    for i in range(len(answers)):
        if answers[i]==soo1[i%5]:
            cnt1+=1
        if answers[i]==soo2[i%8]:
            cnt2+=1
        if answers[i]==soo3[i%10]:
            cnt3+=1
    max_cnt=max(cnt1,cnt2,cnt3)
    max_values=[cnt for cnt in [cnt1,cnt2,cnt3] if cnt==max_cnt]
    for i in range(3):
        if [cnt1,cnt2,cnt3][i]==max_cnt:
            answer.append(i+1)
    answer.sort()
    return answer