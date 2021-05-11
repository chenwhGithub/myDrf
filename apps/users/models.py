from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ''' 账户数据 '''
    GENDER = (
        ('male', u'男'),
        ('female', u'女')
    )

    name = models.CharField(verbose_name='姓名', max_length=30, null=True, blank=True)
    gender = models.CharField(verbose_name='性别', max_length=6, choices=GENDER, default='male')
    birthday = models.DateField(verbose_name='出生年月', null=True, blank=True)

    class Meta:
        db_table = 'df_user'
        verbose_name = '账户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Address(models.Model):
    ''' 地址数据 '''
    user = models.ForeignKey('User', verbose_name='所属用户', on_delete=models.CASCADE)
    receiver = models.CharField(max_length=20, verbose_name='收件人')
    addr = models.CharField(max_length=256, verbose_name='收件地址')
    zip_code = models.CharField(max_length=6, null=True, verbose_name='邮政编码')
    phone = models.CharField(max_length=11, verbose_name='联系电话')
    is_default = models.BooleanField(default=False, verbose_name='是否默认')

    class Meta:
        db_table = 'df_address'
        verbose_name = '地址'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.receiver + ' ' + self.addr
