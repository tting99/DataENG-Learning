import sys
sys.stdin = open('input.txt')

#가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
T = int(input())
for tc in range(1, T + 1):
    # 각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고, NxN의배열에 M크기 파리채
    N, M = map(int, input().split())
    # 다음 N 줄에 걸쳐 N x N 배열이 주어진다.
        #N, M = map(int, input().split())
        # matrix = [1
        #           for _ in range(N):
        # matrix.append(list(map(int, input().split()))) 이 세줄을 컴플리션으로 줄이기 가능
    matrix = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N-M+1):
        pass



    print(f'#{tc} N={N}, M={M}')
    for row in matrix:
        print(row)


print(f'#{tc}')

#미완
