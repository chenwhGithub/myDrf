from rest_framework import serializers
from .models import Goods, Category

# class GoodsSerializer(serializers.Serializer):
    # rest_framework Serializer 实现序列化，属性名必须与 model 定义的一致
    # name = serializers.CharField(required=True, max_length=100)
    # click_num = serializers.IntegerField(default=0)
    # image = serializers.ImageField()


# class GoodsSerializer(serializers.ModelSerializer):
#     # rest_framework ModelSerializer 实现序列化，无需定义字段，只需指定需要序列化的字段即可，但是对于外键不能展开
#     class Meta:
#         model = Goods
#         # fields = '__all__'
#         fields = ['category', 'name', 'click_num', 'sold_num', 'fav_num', 'storage_num', 'price', 'descript', 'image', 'is_hot', 'add_time']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class GoodsSerializer(serializers.ModelSerializer):
    # 外键展开，属性名必须与 model 定义一致
    category = CategorySerializer()
    class Meta:
        model = Goods
        fields = ['category', 'name', 'click_num', 'sold_num', 'fav_num', 'storage_num', 'price', 'descript', 'image', 'is_hot', 'add_time']
