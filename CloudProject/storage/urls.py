from django.urls import path
from . import views

urlpatterns = [
    # 所有文件列表
    path('', views.index, name='index'),

    # 上传界面
    path('upload/', views.upload, name='upload'),

    # 下载链接
    path('download/<file_id>/', views.download, name='download'),

    # 文件删除
    path('delete/<file_id>/', views.delete, name='delete'),

    # 分享的文件
    path('share/', views.share_withlogin, name='share'),

    # 分享文件的下载
    # path('share/<file_id>/', views.download, name='download'),

    # 文件分享激活
    path('share/enable/<file_id>/', views.share_enable, name='share_enable'),

    # 文件分享取消
    path('share/disable/<file_id>/', views.share_disable, name='share_disable'),

    # 文件分享切换
    path('share/switch/<file_id>/', views.share_switch, name='share_switch'),
]
