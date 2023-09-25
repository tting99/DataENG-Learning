from django.urls import path
from . import views #first의 urls는 first로 
#옮겨왔기때문에 자신의를 뜻하는 .을 찍고 임포트. 
# .(나)에 있는 views
urlpatterns = [
    path('hello/', views.hello),   #hello라고 요청이 들오면~
    path('bye/', views.bye),
    path('lotto/', views.lotto),
    path('lunch/', views.lunch),
]

