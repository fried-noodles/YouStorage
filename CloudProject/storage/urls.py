from django.urls import path
from . import views

urlpatterns = [
    # 所有文件列表
    path('', views.index, name='index'),

    # 上传界面
    path('upload/', views.upload, name='upload'),

    # 下载链接
    path('download/<file_id>/', views.download, name='download'),
]
