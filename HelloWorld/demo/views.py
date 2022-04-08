from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from .models import *
import random
# Create your views here.

def toLogic_view(request):
    return render(request,'logic.html')
    
    
# 登录
def login_view(request):
    u = request.POST.get('user','')
    p = request.POST.get('pwd','')

    if u and p:
        c = DemoStudentinfo.objects.filter(std_name=u,std_pwd=p).count()
        if c >= 1:
            return HttpResponse("登录成功!")
        else:
            return HttpResponse("登录失败!")
    else:
        return HttpResponse("请输入正常的账号密码!")

# 渲染注册界面
def toregister_view(request):
    return render(request,'register.html')
    
    

# 注册
def register_view(request):
    u = request.POST.get('user','')
    p = request.POST.get('pwd','')

    if u and p:
        stu = DemoStudentinfo(std_id=random.randrange(0000,9999),std_name=u,std_pwd=p)
        stu.save()
        return HttpResponse("注册成功!")
    else:
        return HttpResponse("请输入正确的账号密码！")