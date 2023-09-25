from django.shortcuts import render
from django.http import HttpResponse    #HttpResponse라는 클래스
# Create your views here.
# 1. function view
# 2. class view
# 이중 함수로 만들거임
import random

def hello(request): #함수를 만들어 보자. 인자로는 request(일반적으로 이래씀)무조건써줘야함
    return render(request,'hello.html') #리턴으로 HttpResponse라는 클래스만 올 수 있다.

def bye(request):
    return render(request,'bye.html') #리턴으로 HttpResponse라는 클래스만 올 수 있다.

def lotto(request):
    lucky_numbers = [random.randint(1, 46) for _ in range(6)]
    lucky_numbers.sort()
    context = {
        'message': 'qqq',
        'lucky_numbers' : lucky_numbers,
    }#데이터넘기는법
    return render(request,'lotto.html', context)


def lunch(request):
    list_food = ['라면','샌드위치','국밥','감자탕']
    randnum = random.randint(0, 3)
    today_lunch = list_food[randnum]
    context = {
        'today_lunch' : today_lunch,
    }
    return render(request,'lunch.html', context)