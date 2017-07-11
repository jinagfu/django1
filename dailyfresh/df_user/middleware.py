# coding=utf-8

from django.http import HttpRequest
# 中间件，定义在视图执行之前对视图或者返回结果进行处理

class UrlPathMiddleware:
	def process_request(self,request):
		path=request.get_full_path()
		path1=request.path
		# 如果当前请求的路径与用户登入/／注册／退出相关，则不需要记录
		if path1 not in ['/user/register/',
			'/user/register_handel/',
			'/user/register_ckname/',
			'/user/login/',
			'/user/logout/',
			'/user/user_islogin/',
			'/user/login_handel/']:
			request.session['url_path']=path   #记录路径



'''
获取访问路径url
request.path
request.get_full_path()
http://www.baidu.com/tuku?name=100
get_full_path(): /tuku?name=100
path: /tuku
'''



























