import sys
sys.stdin = open('input.txt')


def hit(r_index, c_index, size):
    total_val = 0
    for r in range(M):
        for c in range(M):
            total_val += matrix[row + r][col + c]
    return total_val


#가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
T = int(input())
max_val = -float('INF')

for tc in range(1, T + 1):
    N, M = map(int, input().split()) #N크기 배열 M크기 파리채
    matrix = [list(map(int, input().split())) for _ in range(N)]
    for row in range(N-M+1):
        for col in range(N-M+1):
            total = hit(row, col, M)
            if max_val < total:
                max_val = total



   # print(f'#{tc} N={N}, M={M}')
 #   for row in matrix:
       # print(row)


    print(f'#{tc} {max_val}')

#완
#제출시 INF때문에 오류남. 그래도 돌아감.
