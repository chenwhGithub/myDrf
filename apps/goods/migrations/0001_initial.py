# Generated by Django 3.1.1 on 2021-05-11 10:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='类别名', max_length=30, verbose_name='类别名')),
                ('desc', models.TextField(default='', help_text='类别描述', verbose_name='类别描述')),
                ('is_tab', models.BooleanField(default=False, help_text='是否导航', verbose_name='是否导航')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '商品分类',
                'verbose_name_plural': '商品分类',
                'db_table': 'df_category',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(default='', max_length=50, verbose_name='货号')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击量')),
                ('sold_num', models.IntegerField(default=0, verbose_name='销量量')),
                ('fav_num', models.IntegerField(default=0, verbose_name='收藏量')),
                ('storage_num', models.IntegerField(default=0, verbose_name='库存量')),
                ('price', models.FloatField(default=0, verbose_name='价格')),
                ('descript', models.TextField(max_length=500, verbose_name='描述')),
                ('image', models.ImageField(blank=True, null=True, upload_to='goods/images/', verbose_name='封面图')),
                ('is_hot', models.BooleanField(default=False, verbose_name='是否热销')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.category', verbose_name='分类')),
            ],
            options={
                'verbose_name': '商品信息',
                'verbose_name_plural': '商品信息',
                'db_table': 'df_goods',
            },
        ),
    ]
