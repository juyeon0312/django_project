from django.urls import path
from . import views

urlpatterns = [
    # blog 앱 내부의 경로를 지정할 부분
    #localhost:800/경로, 경로를 호출하면 실행할 함수의 위치 작성
    path('', views.index), # 없는 경로를 호출하고 있음 
    path('post-list', views.PostList.as_view()), 
    path('about-me', views.about_me), 
]