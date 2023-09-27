from django.shortcuts import render
from datetime import datetime

def time(request):
    now = datetime.now()
    result = ''
    result += now.strftime("날짜:%Y-%m-%d")
    result += now.strftime("시간:%H:%M:%S")
    result += now.strftime("%A요일")
    context = {
        'now_time':result
    }
    return render(request, 'util/time.html', context)

def index(request):
    return render(request, 'util/index.html')
    
