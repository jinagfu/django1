# coding=utf-8
from haystack.generic_views import SearchView


# 定义 类 ，重写  全文检索的  视图view  --url 重写
class MySearchView(SearchView):
    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        context['title'] = '搜索结果'
        page_obj = context['page_obj'] #获取页面内容对象
        pagelist=[]
        if page_obj.paginator.num_pages<5:
        	pagelist=range(1,page_obj.paginator.num_pages+1)
        elif page_obj.number<=2:
        	pagelist = range(1,5+1)
        elif page_obj.number >= page_obj.paginator.num_pages-1:
        	pagelist = range(page_obj.paginator.num_pages-5+1,page_obj.paginator.num_pages+1)
        else:
        	pagelist = range(page_obj.number-2,page_obj.number+3)
        # 通过上下文将页码传出去
        context['pagelist']=pagelist
        return context





