#coding=utf-8

from django.conf.urls import url
from df_cart import views

urlpatterns = [
	url(r'^$', views.cart),
	url(r'^add/$', views.add),
	url(r'^count/$', views.count),
	url(r'^edit/$', views.edit),  #修改购物车商品的数量
	url(r'^delete/$', views.delete),  #删除购物车商品

]








