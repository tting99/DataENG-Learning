
import sys
sys.stdin = open('input.txt')

#첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
T = int(input())

for tc in range(1, T+1):
    result = [0, 0]
    #다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )
    N = int(input())
    #다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 )
    a = list(input())
    # a_str = input() 이렇게 하지말고 그냥 위 처럼 바로 리스트로 받으면 하나씩 str이 하나씩 들어감
    # a = [int(char) for char in a_str]
    #a = list(input)

    for j in a:
        if a.count(j) > result[1]:
            result[0] = j
            result[1] = a.count(j)
        elif a.count(j) == result[1] and j != result[0]:
            result[0] = max(a)
    print(f'#{tc} {result[0]} {result[1]}')

#완
#제출미완