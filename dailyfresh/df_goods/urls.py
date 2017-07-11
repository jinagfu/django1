# coding=utf-8

from django.conf.urls import url
from df_goods import views
from search_view import MySearchView


urlpatterns=[
	url(r'^index/$', views.index),  #　首页
	url(r'^list(\d+)_(\d*)/$', views.list),  #　商品列表
	url(r'^detail(\d*)/$', views.detail),  #　商品详细信息
	url(r'^search/$',MySearchView.as_view() ),  #　自定义类　视图


]


