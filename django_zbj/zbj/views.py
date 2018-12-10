import hashlib
import numpy
import pandas
import pandas as pd
import numpy as np
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from sklearn.externals import joblib
from sklearn.neighbors import KNeighborsClassifier

from zbj.models import User, Company
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def index(request):
    data = {}
    uid = request.session.get('uid')
    users = User.objects.filter(pk=uid)
    if users.exists():
        user = users.first()
        data['username'] = user.user_name
        data['islog'] = True

    return render(request, 'index.html', context=data)

# 分类页的展示
def classifier(request):
    data = {}
    # 登录状态显示
    uid = request.session.get('uid')
    users = User.objects.filter(pk=uid)
    if users.exists():
        user = users.first()
        data['username'] = user.user_name
        data['islog'] = True
    form_type = request.POST.get('form_type')
    companys = None
    # 根据来源判断需要筛选的公司,生成companys
    if form_type == 'index':
        keyword = request.POST.get('keyword')
        companys = Company.objects.filter(item_title__contains=keyword)
        companys_count = companys.count()

        data['companys_count'] = companys_count
    paginator = Paginator(companys, 20, 10)
    page = request.GET.get('page')
    try:
        companys = paginator.page(page)
    except PageNotAnInteger:
        companys = paginator.page(1)
    except EmptyPage:
        companys = paginator.page(paginator.num_pages)
    data['companys'] = companys
    return render(request, 'classifier.html', context=data)


# md5加密方法
def md5_encipherment(upwd):
    m = hashlib.md5()
    m.update(upwd.encode('utf-8'))
    return m.hexdigest()


def login(request):
    if request.method == 'GET':
        data = {}
        uid = request.session.get('uid')
        users = User.objects.filter(pk=uid)
        if users.exists():
            user = users.first()
            data['username'] = user.user_name
            data['islog'] = True

        return render(request, 'login.html', context=data)

    else:
        # 这是时从login页面的表单跳转过来的 是post请求
        # 获取表单数据
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        # 判断数据库中是否有改用户
        users = User.objects.filter(user_email=user_email)
        if users.exists():
            # user存在，进一步判断密码
            user = users.first()
            if user.user_password == md5_encipherment(user_password):
                # 登录成功
                request.session['uid'] = user.uid
                return redirect(reverse('zbj:index'))
        else:
            # 该用户不存在
            return HttpResponse('用户名密码错误')
        return HttpResponse('用户名密码错误')


# 退出登录 刷新session 重定向到mine页面
def logout(request):
    request.session.flush()
    return redirect(reverse('zbj:index'))


# 注册页面,注册完重定向到主页
def register(request):
    if request.method == 'GET':
        data = {}
        uid = request.session.get('uid')
        users = User.objects.filter(pk=uid)
        if users.exists():
            user = users.first()
            data['username'] = user.user_name
            data['islog'] = True

        return render(request, 'register.html', context=data)

    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        password = md5_encipherment(password)
        username = request.POST.get('username')
        phonenum = request.POST.get('phone')
        user = User()
        user.user_name = username
        user.user_phone = phonenum
        user.user_password = password
        user.user_email = email

        user.save()
        request.session['uid'] = user.uid
        return redirect(reverse('zbj:login'))

def shop(request):
    data = {}
    uid = request.session.get('uid')
    users = User.objects.filter(pk=uid)
    if users.exists():
        user = users.first()
        data['username'] = user.user_name
        data['islog'] = True

    return render(request, 'case.html', context=data)


# def search(request):
#     keyword = request.POST.get('keyword')
#     companys_count = Company.objects.count(item_title__contains=keyword)
#     companys = Company.objects.filter(item_title__contains=keyword)
#     data = {
#         'companys':companys,
#         'companys_count':companys_count
#     }
#     return render(request, 'classifier.html', context=data)


def detail(request, company_id):
    print(company_id)
    print(type(company_id))
    companys = Company.objects.filter(company_id=company_id)
    company = companys.first()
    data = {
        'company':company
    }
    return render(request,'company-details.html', context=data)


def data(request):
    return render(request,'data.html')


def pycharts_good(request):
    return render(request, 'good_mine_zhu.html')


def pycharts_price(request):
    return render(request, 'price_mine_zhu.html')


def pridict(request):
    if request.method == 'GET':
        return render(request, 'predict.html')
    else:
        city = request.POST.get('city')
        yewu = request.POST.get('yewu')

        type_data_all = pd.read_csv('datas.csv')
        type_data = type_data_all[['work_type', 'work_price', 'company_area']]
        # 找出所有的城市
        citys = type_data.company_area.unique()
        # 找出所有的业务类型
        work_type = type_data.work_type.unique()

        # 创建函数，返回查询值的下标
        def city_int(item):
            index = np.argwhere(citys == item)[0, 0]
            return index

        def type_int(item):
            index = np.argwhere(work_type == item)[0, 0]
            return index

        type_data['company_area'] = type_data['company_area'].map(city_int)
        type_data['work_type'] = type_data['work_type'].map(type_int)
        # 取出训练数据
        X_train = type_data[['work_type', 'company_area']]
        Y_train = type_data[['work_price']]
        # 使用KNN近邻算法
        KNN = KNeighborsClassifier(10)
        KNN.fit(X_train, Y_train.astype('int'))
        joblib.dump(KNN, 'yuce.m')
        moxing = joblib.load('yuce.m')
        try:
            city_index = city_int(city)
            typex_index = type_int(yewu)
            X_test = [[city_index, typex_index]]
            y_ = moxing.predict(X_test)[0]
        except Exception as e:
            y_ = 0
        data = {
            'result': y_
        }

        return render(request, 'result-predict.html', context=data)


def show_company(request, comany_type):
    print(comany_type)
    data = {}
    uid = request.session.get('uid')
    users = User.objects.filter(pk=uid)
    if users.exists():
        user = users.first()
        data['username'] = user.user_name
        data['islog'] = True
    companys = Company.objects.filter(item_title__contains=comany_type)
    companys_count = companys.count()
    data['companys_count'] = companys_count
    data['companys'] = companys

    return render(request, 'classifier.html', context=data)