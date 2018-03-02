from django.urls import path
from . import views

urlpatterns = [
    # 所有文件列表
    path('', views.index, name='index'),

    # 上传界面
    path('upload/', views.upload, name='upload'),

    # 下载链接
    path('download/<file_name>/', views.download, name='download'),

    # 分享的文件
    path('share/', views.share_withlogin, name='share'),

    # 分享文件的下载
    path('share/<file_name>/', views.share_down, name='share_down'),

    # 文件分享激活
    path('share/enable/<file_name>/', views.share_enable, name='share_enable'),

    # 文件分享取消
    path('share/disable/<file_name>/', views.share_disable, name='share_disable'),
]
