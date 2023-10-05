from django.shortcuts import render

# Create your views here.

def hello(request, name):
    message = f'{name}님!'
    return render(request, 'user_input/hello.html',
                  {
                      'message':message,
                   })
def ping(request):
    return render(request,'user_input/ping.html')

def pong(request):
    # 받은데이터 딕셔너리 = request.GET
    username = request.GET['username']
    password = request.GET['password']
    return render(request,'user_input/pong.html', {
        'username':username,
        'password':password,
    })