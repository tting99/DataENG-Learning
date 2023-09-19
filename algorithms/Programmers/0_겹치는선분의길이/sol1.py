#https://school.programmers.co.kr/learn/courses/30/lessons/120876
def solution(lines):
    line_hitmap = []
    count = 0
    for _ in range(200):
        line_hitmap.append(0)
    for i in lines:
        for j in range(i[0],i[-1]):
            line_hitmap[j+100] += 1
    for k in line_hitmap:
        if k > 1:
            count += 1
    print(line_hitmap)

    return count

print(solution([[0, 1], [2, 5], [3, 9]])) # 2
print(solution([[-1, 1], [1, 3], [3, 9]])) # 0
print(solution([[0, 5], [3, 9], [1, 10]])) # 8
#완
#제출미완