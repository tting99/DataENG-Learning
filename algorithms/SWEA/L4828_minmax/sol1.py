#https://swexpertacademy.com/main/searchAll/search.do?keyword=min+max
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    answer = max(numbers) - min(numbers)
    print(f'#{tc} {answer}')
    

#완
#제출 완