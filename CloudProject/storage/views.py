from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from .forms import FileUploadForm, FileRec
from django.contrib.auth.decorators import login_required
from .models import UploadFile, FileRec
from django.http import FileResponse

# Create your views here.


@login_required
def index(request):
    file_table = UploadFile.objects.filter(owner=request.user).order_by('-upload_time')
    context = {'files': file_table, 'user': request.user}
    return render(request, 'storage/index.html', context)


@login_required
def upload(request):
    """文件上传"""
    if request.method != 'POST':
        # 未提交数据，创建新表单
        form = FileUploadForm()
    else:
        # 对post提交的数据进行处理
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.owner = request.user
            img = new_form.file_path
            new_form.name = str(img)
            new_form.share_opt = 'False'
            """
            f = open(img.name, 'wb')
            for line in img.chunks():
                f.write(line)
            f.close()
            """
            new_form.save()
            # return HttpResponse('Upload Successfully!')
            return HttpResponseRedirect(reverse('storage:index'))
        return HttpResponseRedirect(reverse('storage:index'))

    context = {'form': form}
    return render(request, 'storage/upload.html', context)


@login_required
def download(request, file_name):
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


@login_required
def share_withlogin(request):
    file_table = UploadFile.objects.filter(share_opt='True', owner=request.user).order_by('-upload_time')
    context = {'files': file_table}
    return render(request, 'storage/share.html', context)


def share_enable(request, file_name):
    UploadFile.objects.filter(owner=request.user, name=file_name).update(share_opt=1)
    # target.share_opt = 'True'
    # target.save()
    # target_pre = UploadFile.objects.get(name=file_name, share_opt=0)
    # target_pre.delete()
    return HttpResponseRedirect(reverse('storage:share'))


def share_disable(request, file_name):
    UploadFile.objects.filter(owner=request.user, name=file_name).update(share_opt=0)
    return HttpResponseRedirect(reverse('storage:share'))


@login_required
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
