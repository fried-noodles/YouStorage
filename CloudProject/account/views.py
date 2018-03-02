from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('homepage:index'))


def register(request):
    """新建用户"""
    if request.method != 'POST':
        # 建立新表单
        form = UserCreationForm()
    else:
        # 处理提交的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # 登录新注册的账号，重新定向到主页
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('homepage:index'))

    context = {'form': form}
    return render(request, 'account/register.html', context)


