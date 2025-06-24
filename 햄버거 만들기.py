# 햄버거 만들기
def solution(ingredient):
    answer = 0
    stack = []
    for x in ingredient:
        stack.append(x)
        if len(stack) >= 4 and \
           stack[-4] == 1 and stack[-3] == 2 and \
           stack[-2] == 3 and stack[-1] == 1:
            answer += 1
            del stack[-4:]
    return answer