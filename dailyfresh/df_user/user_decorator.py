# coding=utf-8
from django.shortcuts import redirect



# 装饰器函数，禁止访问为登入的页面
def isLogin(func):
	def func1(request,*args,**kwargs):
		if request.session.has_key('uname'):
			return func(request)
		else:
			return redirect('/user/login/')
	return func1



