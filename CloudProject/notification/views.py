# _*_ coding=utf-8 _*_
import time
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from .models import Type, Notice
from .form import NoticeForm, TypeForm

# Create your views here.


def index(request):
    """显示全部的通知"""
    # 获取主题
    notice = Notice.objects.order_by('-update_time')
    # 将主题打包成字典
    context = {'notices': notice}
    # 发到前端
    return render(request, 'notification/index.html', context)


def types(request):
    """显示全部的类别"""
    types = Type.objects.order_by('update_time')
    context = {'types': types}
    return render(request, 'notification/types.html', context)


def type(request, type_id):
    """获取全部分组"""
    type = Type.objects.get(id=type_id)
    notices = type.notice_set.order_by('-update_time')
    context = {'type': type, 'notices': notices}

    return render(request, 'notification/type.html', context)


@login_required
def new_type(request):
    """添加新分组"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TypeForm()
    else:
        # POST提交的数据，对数据进行处理
        form = TypeForm(request.POST)
        if form.is_valid():
            new_type = form.save(commit=False)
            new_type.owner = request.user
            new_type.save()
            return HttpResponseRedirect(reverse('notification:types'))

    context = {'form': form}
    return render(request, 'notification/new_type.html', context)


@login_required
def new_notice(request, type_id):
    """在特定列别下新建通知"""
    type = Type.objects.get(id=type_id)
    if request.method != 'POST':
        # 未提交数据，创建新表单
        form = NoticeForm()
    else:
        # 对post提交的数据进行处理
        form = NoticeForm(data=request.POST)
        if form.is_valid():
            new_notice = form.save(commit=False)
            new_notice.type = type
            new_notice.owner = request.user
            new_notice.save()
            return HttpResponseRedirect(reverse('notification:type', args=[type_id]))

    context = {'type': type, 'form': form}
    return render(request, 'notification/new_notice.html', context)


@login_required
def delete_type(request, type_id):
    """删除特定条目"""
    type = Type.objects.get(id=type_id)
    type.delete()
    return HttpResponseRedirect(reverse('notification:types'))


@login_required
def edit_notice(request, notice_id):
    """编辑某一条目"""
    notice = Notice.objects.get(id=notice_id)
    type = notice.type
    if request.method != 'POST':
        # 初次请求，用当前操作条目内容填充表单
        form = NoticeForm(instance=notice)
    else:
        # 对提交的数据进行处理
        form = NoticeForm(instance=notice, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('notification:type', args=[type.id]))

    context = {'type': type, 'notice': notice, 'form': form}
    return render(request, 'notification/edit_notice.html', context)


@login_required
def delete_notice(request, notice_id):
    """删除特定条目"""
    notice = Notice.objects.get(id=notice_id)
    type = notice.type
    notice.delete()
    return HttpResponseRedirect(reverse('notification:type', args=[type.id]))

