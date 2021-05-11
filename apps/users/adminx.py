import xadmin
from xadmin import views
from .models import User, Address
# Register your models here.

class AddressAdmin(object):
    list_display = ['user', 'receiver', 'addr', 'zip_code', 'phone', 'is_default']
    search_fields = ['user', 'receiver', 'addr', 'zip_code', 'phone']
    list_filter = ['user', 'receiver', 'addr', 'zip_code', 'phone', 'is_default']
    ordering = ['-user']
    list_editable = ['receiver', 'addr', 'zip_code', 'phone']
    refresh_times = [3, 5]
    model_icon = 'fa fa-address-card' # http://www.fontawesome.com.cn/faicons/


class GlobalSettings(object):
    site_title = 'myDrf 后台管理界面'
    site_footer = 'wenhui.chen company'
    menu_style = 'accordion'


xadmin.site.register(Address, AddressAdmin)
xadmin.site.register(views.CommAdminView, GlobalSettings)
