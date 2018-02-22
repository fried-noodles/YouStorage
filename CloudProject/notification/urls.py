# _*_ coding=utf-8 _*_
from django.urls import path
from . import views

urlpatterns = [
    # 通知中心首页，显示全部通知
    path('', views.index, name='index'),

    # 通知分组页
    path('Types/', views.types, name='types'),

    # 详细分组下的全部通知页
    path('Type/<type_id>/', views.type, name='type'),

    # 新建分组页
    path('New_type/', views.new_type, name='new_type'),

    # 新建通知页
    path('New_notice/<type_id>/', views.new_notice, name='new_notice'),

    # 编辑通知页
    path('Edit_notice/<notice_id>/', views.edit_notice, name='edit_notice'),

    # 删除功能
    path('Delete_notice/<notice_id>/', views.delete_notice, name='delete_notice'),
    path('Delete_type/<type_id>/', views.delete_type, name='delete_type'),
]