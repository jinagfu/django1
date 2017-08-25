# coding=utf-8
from django.contrib import admin
from models import *
# Register your models here.

class TypeAdmin(admin.ModelAdmin):
	list_display = ['id','ttitle']

class GoodsAdmin(admin.ModelAdmin):
	list_display = ['id', 'gtitle', 'gprice']
	list_per_page = 20


admin.site.register(GoodsInfo,GoodsAdmin)
admin.site.register(TypeInfo,TypeAdmin)








