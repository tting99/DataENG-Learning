#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWYygN36Qn8DFAVm
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())#상자개수,Q회동안
    result_list = [0]*N
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            result_list[j] = i
    result = ' '.join(str(item) for item in result_list)
    print(f'#{tc} {result}')
#완
#제출 완