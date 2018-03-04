# _*_ coding=utf-8 _*_
from django.urls import path
from . import views


urlpatterns = [
    # 首页
    path('', views.index, name='index'),

    # 文件分享
    path('share/', views.share, name='share'),

    # 文件分享的下载
    path('share/<file_name>/', views.download,  name='download'),
]