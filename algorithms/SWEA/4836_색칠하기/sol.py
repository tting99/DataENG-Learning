#https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    count = 0
    base_matrix = [[0] * 10 for _ in range(10)]
    N=int(input())#영역 몇개
    matrix = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(matrix[i][0], matrix[i][2]+1):#x좌표 ex. #T1반복2~4
            for k in range(matrix[i][1], matrix[i][3]+1):#y좌표
                if matrix[i][4] == 1:  # 빨간색이 칠해질때
                    base_matrix[j][k] += 100  #영역어차피 최대 30개 겹칠수 있으니 낭낭하게 100-> 빨간색이 칠해질때는 100입력
                else:
                    base_matrix[j][k] += -1
    # for _ in base_matrix:
    #     print(_)

    for row in range(10):
        for col in range(10):
            if base_matrix[row][col] < 100 and base_matrix[row][col] > 0:
                count += 1
    print(f'#{tc} {count}')
    #완
    #제출완