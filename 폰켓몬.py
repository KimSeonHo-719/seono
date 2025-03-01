def solution(nums):
    answer = 0
    nums.sort()
    cnt=1
    for i in range(len(nums)-1):
        if nums[i]!=nums[i+1]:
            cnt+=1
    n=len(nums)
    if cnt>=n/2:
        answer=n/2
    else:
        answer=cnt
    return answer