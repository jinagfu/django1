# coding=utf-8
from django.shortcuts import render

from django.http import HttpResponse,JsonResponse
from df_goods.models import *
from df_user.models import *
from hashlib import sha1
from django.core.paginator import Paginator

# Create your views here.
# 首页
def index(request):
	# 获取登入用户对象
	# user=UserInfo.objects.get(pk=request.session['uid'])

	# 获取商品lei对象　
	typeList = TypeInfo.objects.all()
	list1=[]
	for temp in typeList:
		goodsList=temp.goodsinfo_set.order_by('-id')[0:4]  #降序排列
		clickList=temp.goodsinfo_set.order_by('-id')[0:4]  #降序排列
		list1.append({'goodsList':goodsList,'clickList':clickList,'tl':temp})
	
	context={'title':'首页','list1':list1}  # 'user':user,
	return render(request, 'df_goods/index.html', context)

# 商品列表
def list(request,pid,pIndex):
	# 获取登入用户对象
	# user=UserInfo.objects.get(pk=request.session['uid']) 
	order = int(request.GET.get('order',1)) #获取排序参数
	desc = int(request.GET.get('desc','1')) #价格排序：降序 或者 升序  *-1 来判断
	
	t1 = TypeInfo.objects.get(pk=int(pid))
	if order == 1:
		glist= t1.goodsinfo_set.all().order_by('-id')
	elif order == 2:

		if desc == 1:
			glist= t1.goodsinfo_set.all().order_by('gprice')
		else:
			glist= t1.goodsinfo_set.all().order_by('-gprice')
	elif order == 3:
		glist= t1.goodsinfo_set.all().order_by('-gclick')
	else:
		order= 1
		glist= t1.goodsinfo_set.all().order_by('-id')

	p = Paginator(glist,2)  #分页列表，每页１０个
	if pIndex == '':
		pIndex = 1
	plist = p.page(int(pIndex)) #第几页内容

	new_list = t1.goodsinfo_set.order_by('-id')[0:2]
	context={'title':'商品列表','t1':t1,'plist':plist,'new_list':new_list,'order':order,'desc':desc}
	return render(request, 'df_goods/list.html',context)


# 商品详细信息
def detail(request,num):
	
	# 获取登入用户对象
	# user=UserInfo.objects.get(pk=request.session['uid']) 
	# 获取商品
	goods = GoodsInfo.objects.get(id=num)
	goods.gclick+=1   #添加点击量＋１
	goods.save()
	click_list=GoodsInfo.objects.filter(gtype=goods.gtype).order_by('-gclick')[0:2]
	context={'title':'商品详情','goods':goods,'list':click_list}  #'user':user,

	# 设置cookie　用于记录　最近浏览　前５个商品
	response = render(request, 'df_goods/detail.html', context)
	ids = request.COOKIES.get('goods_ids','').split(',')
	if num in ids:
		ids.remove(num)
	ids.insert(0,num)
	if len(ids)>5:
		ids.pop()
	response.set_cookie('goods_ids',','.join(ids),max_age=60*60*24*7)
	
	return response








