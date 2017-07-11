# coding=utf-8
from django.db import models
from tinymce.models import HTMLField
# Create your models here.
# 商品类－－６类
class TypeInfo(models.Model):
	ttitle=models.CharField(max_length=10)
	isDelete=models.BooleanField(default=False)

	def __str__(self):
		return self.ttitle.enconde('utf-8')


# 商品信息
class GoodsInfo(models.Model):
	gtitle=models.CharField(max_length=20)
	gpic=models.ImageField(upload_to='goods/')   #上传路径
	#十进制浮点数; max_digits表示总位数; decimal_places表示小数位数
	gprice=models.DecimalField(max_digits=5,decimal_places=2)
	gclick=models.IntegerField()  #点击量
	gunit=models.CharField(max_length=10)  #单位　如：500g／一个／一箱等
	isDelete = models.BooleanField(default=False)
	gsubtitle=models.CharField(max_length=200)  #副标题
	gkucun=models.IntegerField(default=100)  #库存默认１００
	gcontent = HTMLField()  #商品描述
	gtype=models.ForeignKey('TypeInfo')  #外键，商品类型










