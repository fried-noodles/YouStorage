# _*_ coding=utf-8 _*_
from django.urls import path
from django.contrib.auth.views import login


from . import views


urlpatterns = [
    # 登录界面和admin一致
    path('login/', login, {'template_name': 'account/login.html'}, name='login'),

    # 注册界面
    path('register/', views.register, name='register'),

    # 注销界面
    path('logout/', views.logout_view, name='logout'),
]
