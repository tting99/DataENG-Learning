# https://school.programmers.co.kr/learn/courses/30/lessons/120923
import math

def solution(num, total):
    center_num = math.ceil(total/num)
    result = [center_num]

    for i in range(0, int(num/2)):
        result.append(center_num-i-1)
    for j in range(0, int((num-1)/2)):
        result.append(center_num+j+1)
        
    return sorted(result)


print(solution(3, 12))  # [3, 4, 5]
print(solution(5, 15))  # [1, 2, 3, 4, 5]
print(solution(4, 14))  # [2, 3, 4, 5]
print(solution(5, 5))   # [-1, 0, 1, 2, 3]

#완
#제출미완