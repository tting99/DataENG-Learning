import sys
sys.stdin = open('input.txt')

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
T = int(input())
for tc in range(1, T + 1):
    # 각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고, NxN 배열이 주어진다.
    N, M = map(int, input().split())
    # NxN 배열을 입력 받을 때는 반복문을 통해 한 줄씩 받도록 합니다.
    matirx = [list(map(int, input().split())) for _ in range(N)]
    # matrix = []
    # for _ in range(N):
    #     row = list(map(int, input().split()))
    #     matrix.append(row)

    # 이후 파리채의 크기 M에 따른 계산 로직을 작성하면 됩니다.
    # 파리채와 NxN 배열이 모두 주어진 후에 계산을 수행하는 것이 적절할 것입니다.

    # 예시로 파리채의 크기 M을 출력해보겠습니다.
    print(f'#{tc} N={N}, M={M}')
    for row in matrix:
        print(row)
