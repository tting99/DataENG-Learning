#https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import sys
sys.stdin = open('input.txt')
# 테스트케이스( 1 ≤ T ≤ 50 )
T = int(input())
for tc in range(1,T+1):
    max_sum = 0
    min_sum = 100000
    N, M = map(int, input().split())  #정수의 개수 ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N ), 구간의 개수(M개 뽑아)
    #n개의 정수( 1 ≤ a ≤ 10000 )
    a = list(map(int, input().split()))
    for i in range(N-M+1):
        max_sum = max(max_sum, sum(a[i:i+M]))
        min_sum = min(min_sum, sum(a[i:i+M]))

    print(f'#{tc} {max_sum - min_sum}')

#완
#제출미완