"""
URL configuration for intro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include   #first앱에 대한 urls는 first앱 안에 urls에서 처리할거
#그렇기때문에 그곳에 urls를 다 옮기고 여기랑 이어줘야 한다.(포워딩)
#import path뒤에 include를 더 붙이고 아래로 가서 path('x/', include('first_app.urls')),작성
#이러면 x뒤에/lotto이런식으로 주소를 입력하면 나온다. x는 임시값임 맘대로



urlpatterns = [
    path('admin/', admin.site.urls),
    #path('x/', include('first_app.urls')), 보통은 이름 아래처럼 하자.
    path('first_app/', include('first_app.urls')), #first_app이라는 요청이 들어오면 first_app.url에 넘겨주겠다. 
    path('second_app/', include('second_app.urls')),
    # Req => ('요청url', 함수) 요청
    # Res => () 응답
]
