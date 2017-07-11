#coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum
from df_goods.models import *
from df_cart.models import *
from df_user.user_decorator import isLogin

# Create your views here.

@isLogin
def cart(request):
	uid = request.session.get('uid')
	cart_list=CartInfo.objects.filter(user_id=uid)

	context={'title':'购物车','search':'0','cart_list':cart_list}
	return render(request,'df_cart/cart.html',context)


def add(request):
	try:
		uid = request.session.get('uid')
		gid = int(request.GET.get('gid'))
		count = int(request.GET.get('count','1'))

		cart = CartInfo.objects.filter(user_id=uid,goods_id=gid)
		if len(cart) == 1:#如果用户uid已经购买了商品gid，则将数量+count
			cart[0].count+=count
			cart[0].save()
		else:
			cart = CartInfo()
			cart.user_id = uid  #注意是user_id 不是user
			cart.goods_id = gid
			cart.count = count 
			cart.save()
		return JsonResponse({'isadd':1})

	except Exception:
		return JsonResponse({'isadd':0})
	
def count(request):
	uid = int(request.session.get('uid'))
	count1 = CartInfo.objects.filter(user_id=uid).count()
	# count1=CartInfo.objects.filter(user_id=uid).aggregate(Sum('count')).get('count__sum')#字典
	return JsonResponse({"count":count1})







