from django.shortcuts import render
from datetime import date


# Create your views here.
def is_xmas(request):
    def is_specific_date(date_to_check):
        today = date.today()
        return today == date_to_check

    # 특정 날짜 생성 (예: 12월 25일)
    specific_date = date(date.today().year, 12, 25)

    # 함수 호출 및 결과 확인
    if is_specific_date(specific_date):
        result = '오늘은 크리스마스입니다.'
    else:
        result = '오늘은 크리스마스가 아닙니다.'
    context = {
        'is_xmas':result
    }
    return render(request, 'is_xmas.html', context)

def fibo(request):
    def fibo_fn(n):
        fib_list = [0, 1]  # 초기 두 항을 포함한 리스트

        for i in range(2, n + 1):
            next_fib = fib_list[i - 1] + fib_list[i - 2]
            fib_list.append(next_fib)

        return fib_list[:n + 1]  # 0부터 n까지의 항만 포함된 리스트 반환
    fibo_list = fibo_fn(30)
    context = {
        'fibo_list_to30' : fibo_list
    }
    return render(request, 'fibo.html', context)
