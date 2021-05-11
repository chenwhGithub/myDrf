import xadmin
from xadmin import views
from .models import Category, Goods
# Register your models here.

class CategoryAdmin(object):
    list_display = ['name', 'desc', 'is_tab', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'is_tab']
    ordering = ['-name']
    model_icon = 'fa fa-desktop'


class GoodsAdmin(object):
    list_display = ['category', 'sn', 'name', 'click_num', 'sold_num', 'fav_num', 'storage_num', 'price', 'descript', 'image', 'is_hot', 'add_time']
    search_fields = ['category', 'sn', 'name', 'descript']
    list_filter = ['category', 'name', 'price', 'descript', 'is_hot']
    ordering = ['-name']
    model_icon = 'fa fa-hourglass'


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Goods, GoodsAdmin)
