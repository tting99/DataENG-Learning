#https://www.acmicpc.net/problem/1244
import sys
sys.stdin = open('input.txt')

num_of_switch = int(input())
switches = list(map(int, input().split()))
#학생수
m = int(input())

student = []
for _ in range(m):
    gender, num = map(int, input().split())
    student.append((gender, num))
#꿀팁 인덱스 헷갈리니까 애초에 idx = num_of_switch - 1
for i in student:
    #i = (1, 3)
    if i[0] == 1:   #남자라면
        for j in range(i[1], num_of_switch+1, i[1]):    #입력받은 수부터 끝까지.
            switches[j-1] = 1 - switches[j-1]
        print(switches)
    else:
        left, right = i[1]-2, i[1]
        while (left != -1 and right != len(switches)):
            if switches[left] == switches[right]:
                switches[left] = 1 - switches[left]
                #꿀팁! 파이썬에 XOR있다 -> switches[] ^= 1
                #또는 switches[idx] = 0 if switches[idx] else 1
                switches[right] = switches[left]
                left -= 1
                right += 1
            else:
                break
print(switches)

#완
#제출 미완 (문제가 나랑 이해한것이 다름. 정답 찾아보고 여학생 스위치 로직의 의미가 뭔지 알것)