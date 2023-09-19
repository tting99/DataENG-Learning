#https://www.acmicpc.net/problem/2562
import sys
sys.stdin = open('input.txt')
numbers = []

# for _ in range(9):
#     x = int(input())
#     numbers.append(x)
numbers = [int(input()) for _ in range(9)]

max_val = max(numbers)
location = numbers.index(max_val) + 1

print(max(numbers))

#미완 몇번째 수인지 출력할것
