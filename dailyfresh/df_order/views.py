# coding=utf-8
from django.shortcuts import render,redirect
from df_order.models import *
from df_cart.models import *
from df_user.models import *
from df_user.user_decorator import isLogin
import datetime
# 导入事务管理
from django.db import transaction
# Create your views here.

def order(request):
	user = UserInfo.objects.get(id=request.session.get('uid'))

	id_list = request.POST.getlist('cart_id')
	cart_list = CartInfo.objects.filter(id__in=id_list)
	
	context={'title':'提交订单','user':user,'cart_list':cart_list,'search':'0','cart_id_list':','.join(id_list)}
	return render(request,'df_order/order.html',context)

# 提交订单后的处理－－注意使用事务
@transaction.atomic
def do_order(request):
	# 创建事务监听点savepoint
	sid = transaction.savepoint()
	total_all = 0
	is_commit = True

	try:
		cart_id_list = request.POST.get('cart_id_list').split(',')
		
		# 创建主订单类
		order_mian = OrderMain()
		# 订单时间，　　转成字符串格式化　strftime()　注意参数
		order_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
		uid = request.session.get('uid')
		order_mian.orderid = '%s%d'%(order_time,uid)
		# order_mian.order_time = order_time 自动添加　无须设置# atomic()　在块结束前不能执行查询　－－此处相当于修改值update
		order_mian.user_id = uid
		order_mian.save()
		# 便利购物车对象
		for cart in CartInfo.objects.filter(id__in=cart_id_list):
			# 判断购买量　和　库存量
			if cart.count <= cart.goods.gkucun:
				detail = OrderDetail()  #创建详单
				detail.order_id = order_mian.orderid
				detail.goods_id = cart.goods.id
				detail.count = cart.count
				detail.price = cart.goods.gprice
				# 商品小计
				total_all+= cart.count*cart.goods.gprice
				detail.save()  # atomic()　在块结束前不能执行查询
				# 修改商品库存
				cart.goods.gkucun -= cart.count
				cart.goods.save()
				# 删除购物车商品数据
				cart.delete()
			else:
				# 商品库存不足
				transaction.savepoint_rollback(sid)
				is_commit=False
				break
		if is_commit:
			order_mian.total = total_all  #　订单总价
			order_mian.save()
			transaction.savepoint_commit(sid)
	except Exception as e:
		print(e)
		is_commit=False
		# 回滚事物保存点sid.
		transaction.savepoint_rollback(sid)
		

	if is_commit:
		return redirect('/user/order/')
	else:
		return redirect('/cart/')


	








