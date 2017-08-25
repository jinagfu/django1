# coding=utf-8
from django.db import models
from df_user.models import UserInfo
# Create your models here.


class CartInfo(models.Model):
    goods=models.ForeignKey('df_goods.GoodsInfo')
    user=models.ForeignKey(UserInfo)
    count=models.IntegerField()



