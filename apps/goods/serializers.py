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
    # 外键处理，当序列化与反序列化的类型不同时，需要分别生成 read_only 和 write_only 两个字段
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Goods
        # fields = '__all__'
        fields = ['category', 'category_id', 'name', 'click_num', 'sold_num', 'fav_num', 'storage_num', 'price', 'descript', 'image', 'is_hot', 'add_time']

    def create(self, validated_data):
        # POST 消息处理中 goods_serialzer.save() 调用
        category_obj = Category.objects.get(id=validated_data['category_id'])
        goods_obj = Goods.objects.create(category=category_obj, **validated_data)
        return goods_obj
