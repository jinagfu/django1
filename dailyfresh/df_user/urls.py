# coding=utf-8

from django.conf.urls import url
from df_user import views

urlpatterns=[
	url(r'^register/$', views.register),  #　用户注册
	url(r'^register_handel/$', views.register_handel),  #　用户注册处理
	url(r'^register_ckname/$', views.register_ckname),  #　用户注册处理
	url(r'^login/$', views.login),  #　用户登入
	url(r'^login_handel/$', views.login_handel),  #　用户登入处理
	url(r'^center/$', views.center),  #　用户中心页
	url(r'^order/$', views.order),  #　用户全部订单
	url(r'^site/$', views.site),  #　用户收货地址／添加地址信息
	url(r'^logout/$', views.logout),  #　用户退出
	url(r'^user_islogin/$', views.user_islogin),  #　判断登入－－ｌｉｓｔ中



]


















