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
def download(request, file_id):
    # form = FileRec()
    file = UploadFile.objects.get(id=file_id)
    path = file.file_path
    # form.oprtr = request.user
    # form.file = str(file.name)
    # form.save()
    response = FileResponse(path)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file.name)
    return response
