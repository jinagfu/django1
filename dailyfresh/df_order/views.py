# coding=utf-8
from django.shortcuts import render
from df_order.models import *
from df_cart.models import *
from df_user.models import *
from df_user.user_decorator import isLogin
# Create your views here.

def order(request):
	user = UserInfo.objects.get(id=request.session.get('uid'))

	id_list = request.POST.getlist('cart_id')
	cart_list = CartInfo.objects.filter(id__in=id_list)
	
	context={'title':'提交订单','user':user,'cart_list':cart_list,'search':'0'}
	return render(request,'df_order/order.html',context)









