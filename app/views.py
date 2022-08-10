import json
from app.models import KeSuanInfo
from app.models import ShopInfo
from django.contrib.sessions import serializers
from django.http.response import JsonResponse
from django.core import serializers
import json
# Create your views here.
from django.shortcuts import render, HttpResponse
from scipy.sparse import data

from app.models import UserInfo
from app.models import kuchunINfo
from app.models import jinhuoINFo


def index(request):
    return HttpResponse("hello")


def user_list(request):
    return render(request, "user_list.html")


def orm(request):
    article = serializers.serialize('json', UserInfo.objects.all()[:5])
    # 将字符串转换为json对象
    jsondata = json.loads(article)
    # 将data放入字典中
    data = {
        'data': jsondata,
        'code': '200',
        'message': '获取成功!'
    }
    # 返回前端json
    return JsonResponse(data=data, safe=False)


def denglu(request):
    return render(request, "login.html")


def loginHello(request):
    if request.method == "GET":
        name = request.GET.get('username')
        password = request.GET.get('password')
        print(name)
        print(password)

        users = UserInfo.objects.filter(name=name)
        user = users.first()
        print(user.name)
        print(user.password)
        if name == user.name and password == user.password:
            print("登录成功")
            # data_list =KeSuanInfo.objects.filter(name=name).all()
            data_list = KeSuanInfo.objects.all()
            return render(request, "user_list.html", {"data_list": data_list})


def select(request):
    name = request.GET.get('username')
    print(name)
    data_list = KeSuanInfo.objects.filter(name=name).all()
    return render(request, "user_list.html", {"data_list": data_list})


# def kesuan(request):

def shopINfo(request):
    # data_list =KeSuanInfo.objects.filter(name=name).all()
    data_list = ShopInfo.objects.all()
    print("ssss")
    return render(request, "shop_list.html", {"data_list": data_list})


def jinhuo(request):
    # data_list =KeSuanInfo.objects.filter(name=name).all()
    data_list =jinhuoINFo.objects.all()
    print("ssss")
    return render(request, "jinhuo_list.html", {"data_list": data_list})


def kucun(request):
    # data_list =KeSuanInfo.objects.filter(name=name).all()
    data_list = kuchunINfo.objects.all()

    print("ssss")
    return render(request, "kucun_list.html", {"data_list": data_list})
# def kesuan(request):

def jiating(request):
    return render(request, "jiating.html")


def register1(request):
    if request.method == "GET":
        name = request.GET.get("username")
        password = request.GET.get("password")
        # address = request.POST.get("adress")
        # age = request.POST.get("age")
        # number = request.POST.get("number")
        # jiating = request.POST.get("jiating")
        # vaccine = request.POST.get("vaccine")
        # kesuan = request.POST.get("kesuan")
        # jinzhu = request.POST.get("jinzhu")
        UserInfo.objects.create(name=name, password=password)
        # data = {
        #     'flag': 1,
        #     'code': '200',
        #     'message': '获取成功!'
        # }
        return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def info(request):
    article = serializers.serialize('json', KeSuanInfo.objects.all()[:5])
    # 将字符串转换为json对象
    jsondata = json.loads(article)
    # 将data放入字典中
    data = {
        'data': jsondata,
        'code': '200',
        'message': '获取成功!'
    }
    # 返回前端json
    return JsonResponse(data=data, safe=False)


def update(request):
    id = request.GET.get("id")
    KeSuanInfo.objects.filter(id=id).update(kesuan='ok', is_active=True)
    KeSuanInfo.objects.filter(id=id).delete()
