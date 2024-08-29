from django.urls import path
from . import views

app_name = 'blog_app' #blog_app:blog -> localhost:8000/blog/poset-list

urlpatterns = [
    # blog 앱 내부의 경로를 지정할 부분
    #localhost:800/경로, 경로를 호출하면 실행할 함수의 위치 작성
    #path('', views.index), # 없는 경로를 호출하고 있음 
    path('post-list', views.PostList.as_view(), name = 'post_list'), 
    path('', views.about_me, name = 'about_me'), 
    path('<int:pk>', views.PostDetail.as_view()), #<자료형: 필드명>
    path('create-post/', views.PostCreate.as_view(), name = 'create'),
    path('user-delete/', views.user_delete, name='user_delete') # blog_app:user_delete
]