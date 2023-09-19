#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())#NxN

    matrix = [[0]*N for _ in range(N)]
    d_rows = [0, 1, 0, -1]#1하3상
    d_cols = [1, 0, -1, 0]#0우2좌
    direction = 0

    row = col = 0     # 현재 좌표값(시작위치 => 0, 0)

    # 첫 칸 숫자는 채우고 시작 -> 이유:채우고 전진하냐vs전진하고 채우냐 - 근데 전진하고 채워야 한다.


    # num 은 앞으로 채울 숫자
    num = 1
    matrix[row][col] = num
    while num != N ** 2:        # 새로운 row/col 좌표값 생성
        new_row = row + d_rows[direction]
        new_col = col + d_cols[direction]

        # 새로운 좌표값은 0 이상 N 미만 and 채우려는 칸이 비어있어야 (0) 한다.
        if 0 <= new_row < N and 0 <= new_col < N and matrix[new_row][new_col] == 0:
            #다음 숫자로 바꿈
            num += 1
            # 새로운 좌표값에 num을 채운다.
            matrix[new_row][new_col] = num
            # 현재의 좌표값을 새로운 좌표값으로 갱신한다.
            row, col = new_row, new_col
        # 위 조건을 만족하지 않으면
        else:
            # delta 방향(direction) 을 조정한다.
            direction = (direction + 1) % 4

    print(f'#{tc}')
    for i in range(N):
        print(*matrix[i])

#완 / 내가다시 해볼것
#제출미완