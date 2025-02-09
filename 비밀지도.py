def binary(n, num):
    binary_list=[bin(num)[2:]]
    return binary_list[0].zfill(n)
def solution(n, arr1, arr2):
    answer = []
    square1=[binary(n,arr1[i]) for i in range(n)]
    square2=[binary(n,arr2[i]) for i in range(n)]
    for i in range(n):
        row=""
        for j in range(n):
            if square1[i][j]=="1" or square2[i][j]=="1":
                row+="#"
            else:
                row+=" "
        answer.append(row)
    return answer