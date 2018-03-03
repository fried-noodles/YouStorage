from django.shortcuts import render
from django.http import FileResponse
from django.contrib.auth.decorators import login_required


from notification.models import Notice
from storage.models import UploadFile, FileRec

# Create your views here.


def index(request):
    """显示全部的通知"""
    # 获取主题
    notice = Notice.objects.order_by('-update_time')
    context = {'notices': notice}

    return render(request, 'homepage/index.html', context)


@login_required
def share(request):
    file_table = UploadFile.objects.filter(share_opt='True').order_by('-upload_time')
    context = {'files': file_table}
    return render(request, 'homepage/share.html', context)


"""
def share_down(request, file_name):
    form = FileRec()
    file = UploadFile.objects.get(name=file_name)
    path = file.file_path
    form.oprtr = request.user
    form.file = str(file.name)
    form.type = 'D'
    form.save()
    response = FileResponse(path)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file.name)
    return response
"""
