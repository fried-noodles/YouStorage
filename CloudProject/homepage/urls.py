# _*_ coding=utf-8 _*_
from django.urls import path
from . import views


urlpatterns = [
    # 首页
    path('', views.index, name='index'),
]