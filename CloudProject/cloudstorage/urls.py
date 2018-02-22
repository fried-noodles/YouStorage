"""cloudstorage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # 站点管理
    path('admin/', admin.site.urls),

    # 主页面
    path('', include(('homepage.urls', 'homepage'), namespace=None)),

    # 消息
    path('notification/', include(('notification.urls', 'notification'), namespace=None)),

    # 账户管理
    path('account/', include(('account.urls', 'account'), namespace=None)),

    # 储存服务
    path('storage/', include(('storage.urls', 'storage'), namespace=None)),

]
