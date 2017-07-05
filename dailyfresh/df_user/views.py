# coding=utf-8
from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse,JsonResponse
from df_user.models import *
from hashlib import sha1
import datetime


# 用户注册视图函数
def register(request):
	context = {'title':'注册','top':'0'}
	return render(request, 'df_user/register.html', context)

# 用户注册提交处理
def register_handel(request):
	# 获取用户注册信息
	post = request.POST
	user_name = post.get('user_name')
	pwd = post.get('pwd')
	cpwd = post.get('cpwd')
	email = post.get('email')
	# 密码加密
	s1 = sha1()
	s1.update(pwd)
	pwd_sha1 = s1.hexdigest()

	# 向数据库保存数据，判断用户名是否以存在
	user=UserInfo()
	user.uname = user_name
	user.upwd = pwd_sha1
	user.umeil = email
	user.save()  #　保存数据
	#重定向到登录页
	return redirect('/user/login/')

# 验证用户名是否已经存在
def register_ckname(request):
	uname = request.GET.get('uname')  #接收用户名
	# 查询该用户名在数据库中的个数
	date = UserInfo.objects.filter(uname=uname).count()
	# 返回查询结果到ｈｔｍｌ中
	context = {"valid":date}
	return JsonResponse(context)

# 用户登入视图函数
def login(request):
	context = {'title':'登入','top':'0'}
	return render(request, 'df_user/login.html',context)
#　用户登入处理验证
def login_handel(request):
	# 获取用户输入信息
	post = request.POST
	username = post.get('username')
	pwd = post.get('pwd')
	checkbox = post.get('checkbox','0')  #默认值‘０’
	# 密码加密
	s1 = sha1()
	s1.update(pwd)
	pwd_sha1 = s1.hexdigest()
	context={'title':'登入','top':'0'}
	# 判断用户名和密码是否正确
	user = UserInfo.objects.filter(uname=username)
	if len(user) > 0:
		if user[0].upwd==pwd_sha1:
			response=redirect('/user/center/')
			if checkbox == '1':
				response.set_cookie('username',username, expires=datetime.datetime.now() + datetime.timedelta(days = 14))
			else:
				response.set_cookie('username','',max_age=-1)
			return response
		else:
			context['pwd_error'] = '密码错误！'
			return render(request, 'df_user/login.html', context)
	else:
		context['name_error'] = '用户名不存在！'
		return render(request, 'df_user/login.html', context)



def center(request):
	context={'title':'用户信息'}
	return render(request, 'df_user/center.html',context)



def order(request):
	context={'title':'全部订单'}
	return render(request, 'df_user/order.html',context)


def site(request):
	context={'title':'收货地址'}
	return render(request, 'df_user/site.html',context)



















