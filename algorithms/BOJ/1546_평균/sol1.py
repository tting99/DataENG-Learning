#https://www.acmicpc.net/problem/1546

#과목명
n = int(input())
score = list(map(int, input().split()))
high_score = max(score)
result_list = []
for i in score:
    result_list.append(i/high_score*100)
print(sum(result_list)/len(result_list))

# 입력
# 9
# 10 20 30 40 50 60 70 80 90


#완료
#제출 완