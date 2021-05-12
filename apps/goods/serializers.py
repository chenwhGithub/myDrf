from rest_framework import serializers
from .models import Goods, Category

class CategorySerializer(serializers.ModelSerializer):
    ''' Category 数据表序列化类 '''
    class Meta:
        model = Category
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):
    ''' Goods 数据表序列化类 '''
    # 外键处理，当序列化与反序列化的类型不同时，需要分别生成 read_only 和 write_only 两个字段
    category = CategorySerializer(read_only=True) # 序列化
    category_id = serializers.IntegerField(write_only=True) # 反序列化，HTTP 请求携带字段 "category_id": 3

    class Meta:
        model = Goods
        # fields = '__all__'
        fields = ['category', 'category_id', 'name', 'click_num', 'sold_num', 'fav_num',
                  'storage_num', 'price', 'descript', 'image', 'is_hot', 'add_time']

    def create(self, validated_data):
        cat_id = validated_data.pop('category_id')
        goods_obj = Goods.objects.create(category_id=cat_id, **validated_data)
        return goods_obj
