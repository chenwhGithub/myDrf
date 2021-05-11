from datetime import datetime
from django.db import models

# Create your models here.
class Category(models.Model):
    ''' 商品分类 '''
    name = models.CharField(verbose_name='类别名', default='', max_length=30, help_text='类别名')
    desc = models.TextField(verbose_name='类别描述', default='', help_text='类别描述')
    is_tab = models.BooleanField(verbose_name='是否导航', default=False, help_text='是否导航')
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        db_table = 'df_category'
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    ''' 商品信息 '''
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='分类')
    sn = models.CharField(verbose_name='货号', max_length=50, default='')
    name = models.CharField(verbose_name='名称', max_length=100)
    click_num = models.IntegerField(verbose_name='点击量', default=0)
    sold_num = models.IntegerField(verbose_name='销量量', default=0)
    fav_num = models.IntegerField(verbose_name='收藏量', default=0)
    storage_num = models.IntegerField(verbose_name='库存量', default=0)
    price = models.FloatField(verbose_name='价格', default=0)
    descript = models.TextField(verbose_name='描述', max_length=500)
    image = models.ImageField(verbose_name='封面图', upload_to='goods/images/', null=True, blank=True)
    is_hot = models.BooleanField(verbose_name='是否热销', default=False)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        db_table = 'df_goods'
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
