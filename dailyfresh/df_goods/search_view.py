# coding=utf-8
from haystack.generic_views import SearchView


# 定义 类 ，重写  全文检索的  视图view  --url 重写
class MySearchView(SearchView):
    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        context['title'] = '搜索结果'
        return context





