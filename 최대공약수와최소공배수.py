def solution(n, m):
    answer = []
    tmp1=n
    tmp2=m
    r=1
    while r>0:
        r=tmp1%tmp2
        tmp2=r
    gcd=tmp1
    lcm=n*m/gcd
    answer.append(gcd)
    answer.append(lcm)
    return answer