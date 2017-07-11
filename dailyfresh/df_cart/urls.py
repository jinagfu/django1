#coding=utf-8

from django.conf.urls import url
from df_cart import views

urlpatterns = [
	url(r'^$', views.cart),
	url(r'^add/$', views.add),
	url(r'^count/$', views.count),

]








