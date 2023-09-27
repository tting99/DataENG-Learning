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
    return render(request,'user_input/pong.html')