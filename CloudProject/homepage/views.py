from django.shortcuts import render
from notification.models import Notice

# Create your views here.


def index(request):
    """显示全部的通知"""
    # 获取主题
    notice = Notice.objects.order_by('-update_time')
    context = {'notices': notice}

    return render(request, 'homepage/index.html', context)