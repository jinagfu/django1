# coding=utf-8
from django.db import models

# Create your models here.

class UserInfo(models.Model):
	uname = models.CharField(max_length=20)
	upwd = models.CharField(max_length=40)

	def __str__(self):
		return "%d" %self.pk  # ｐｋ默认的主键ｉｄ别名
		














