#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    result = 0
    order_amount = 0
    value = 0
    N = int(input())    #N일동안 매매
    prices = list(map(int, input().split()))
    start_idx = 0
    end_idx = N-1
    while start_idx < N-1: #N일동안만 반복
        if prices[start_idx] == max(prices[start_idx:]):
            start_idx += 1
        else:
            end_idx = prices.index(max(prices[start_idx:]))
            for i in range(start_idx, end_idx):   #최댓값 전까지는
                value += prices[i]
                order_amount += 1
            result += prices[end_idx] * order_amount - value
            value = 0
            order_amount = 0
            start_idx = end_idx + 1
            end_idx = N-1
    print(f'#{tc} {result}')

#완
#제출시 오류