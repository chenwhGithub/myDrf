from rest_framework import serializers
from rest_framework.exceptions import ValidationError
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
        fields = ['id', 'category', 'category_id', 'name', 'click_num', 'sold_num', 'fav_num',
                  'storage_num', 'price', 'descript', 'image', 'is_hot', 'add_time']
        extra_kwargs = {
            'price': {
                'required': True, # 设置字段静态校验规则，通常在 model 中定义即可
                'max_value': 9999,
                'error_messages': {
                    # 设置 Response(serialzer.errors) 返回的错误信息，如下：
                    # {
                    #     "price": [
                    #         "price 字段是必填项"
                    #     ]
                    # }
                    'required': 'price 字段是必填项',
                    'max_value': '价格不能大于 9999',
                }
            }
        }

    # 局部钩子，单个字段逻辑校验，函数名格式：validate_字段名
    def validate_name(self, value):
        if 'hello' in value.lower():
            # 设置 Response(serialzer.errors) 返回的错误信息，如下：
            # {
            #     "name": [
            #         "名字不能包含 hello 字符"
            #     ]
            # }
            raise ValidationError('名字不能包含 hello 字符')
        return value

    # 全局钩子，所有字段逻辑校验，可以对多个字段进行联合校验
    def validate(self, attrs):
        cat_id = attrs.get('category_id')
        name = attrs.get('name')
        if Goods.objects.filter(name=name, category_id=cat_id):
            # 设置 Response(serialzer.errors) 返回的错误信息，如下：
            # {
            #     "name_and_category_id": [
            #         "名字和分类都相同，该书已存在"
            #     ]
            # }
            raise ValidationError({'name_and_category_id':'名字和分类都相同，该书已存在'})
        return attrs

    def create(self, validated_data):
        cat_id = validated_data.pop('category_id')
        goods_obj = Goods.objects.create(category_id=cat_id, **validated_data)
        return goods_obj
