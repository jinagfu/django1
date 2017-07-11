# coding=utf-8
from django.shortcuts import render,redirect
from user_decorator import isLogin
# Create your views here.
from django.http import HttpResponse,JsonResponse
from df_user.models import *
from df_goods.models import *
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
	# 判断用户名和密码是否正确   返回的是个一个列表信息
	user = UserInfo.objects.filter(uname=username)
	if len(user) > 0:
		if user[0].upwd==pwd_sha1:
			# response=redirect('/user/center/')
							#　从自定义中间件获取地址　设置默认地址：/user/center/
			response=redirect(request.session.get('url_path','/user/center/'))
			# #登入用户记录下来　　　　－－－－－－－－－－－－－－－－－－－－－
			request.session['uid']=user[0].id  
			request.session['uname']=user[0].uname
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


# 判断是否登入
def user_islogin(request):
	result = 0
	if request.session.has_key('uid'):
		result = 1
	return JsonResponse({"result":result})



# 用户中心－－个人信息
@isLogin  #装饰器，未登入页不能访问，跳转到登入页
def center(request):
	# filter查找结果是QuerySet，一个列表
	user=UserInfo.objects.get(pk=request.session['uid'])
	# 浏览商品列对象
	ids = request.COOKIES.get('goods_ids','').split(',') #[:-1]最后一个是''
	glist = []
	for gid in ids:
		glist.append(GoodsInfo.objects.get(id=gid))

	context={'title':'用户中心','username':user.uname,'uphone':user.uphone,'ucode':user.ucode,'search':'0','glist':glist}
	return render(request, 'df_user/center.html',context)

# 订单信息
@isLogin
def order(request):
	context={'title':'用户中心','search':'0'}
	return render(request, 'df_user/order.html',context)

# 收货地址
@isLogin
def site(request):
	user=UserInfo.objects.get(pk=request.session['uid'])
	#post请求，修改当前用户对象的收货信息
	if request.method == 'POST':
		# 获取用户提交的收货信息
		post = request.POST
		shouname = post.get('shouname')
		shouadd = post.get('shouadd')
		shoucode = post.get('shoucode')
		shouphone = post.get('shouphone')
		# 添加或修改数据库中的信息
		user.uaddress=shouadd
		user.ushou=shouname
		user.ucode=shoucode
		user.uphone=shouphone
		user.save()
	context={'title':'用户中心','user':user,'search':'0'}	
	return render(request, 'df_user/site.html',context)

# 用户退出
def logout(request):
	# 退出删除所有的ｓｅｓｓｉｏｎ记录
	request.session.flush()
	return redirect('/user/login/')  #重定向到登入页面





	




















