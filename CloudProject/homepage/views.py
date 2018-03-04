from django.shortcuts import render
from django.http import FileResponse
from django.contrib.auth.models import User


from notification.models import Notice
from storage.models import UploadFile, FileRec

# Create your views here.


def index(request):
    """显示全部的通知"""
    # 获取主题
    notice = Notice.objects.order_by('-update_time')
    context = {'notices': notice}

    return render(request, 'homepage/index.html', context)


def share(request):
    file_table = UploadFile.objects.filter(share_opt='True').order_by('-upload_time')
    context = {'files': file_table}
    return render(request, 'homepage/share.html', context)


def download(request, file_name):
    form = FileRec()
    file = UploadFile.objects.get(name=file_name)
    path = file.file_path
    if User.is_authenticated:
        form.oprtr = request.user
    else:
        form.oprtr = 0
    form.file = str(file.name)
    form.type = 'D'
    form.save()
    response = FileResponse(path)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file.name)
    return response

